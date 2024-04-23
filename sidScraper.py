import requests
from bs4 import BeautifulSoup
import json

url = "https://parents.msrit.edu/newparents/index.php"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
USN = "1MS21CI055"
payload = {
    "username": USN,
    "dd": "24",
    "mm": "03",
    "yyyy": "2003",
    "passwd": "2003-03-24",
    "remember": "",
    "option": "com_user",
    "task": "login",
    "return": "",
    "ea07d18ec2752bcca07e20a852d96337": "1"
}


def calculate_classes(absent, present, still_to_go, required_attendance=75):
    try:
        absent = int(absent) if absent is not None else 0
        present = int(present) if present is not None else 0
        still_to_go = int(still_to_go) if still_to_go is not None else 0

        total_classes = present + absent + still_to_go
        max_absent = total_classes * (1 - required_attendance / 100) - absent
        return max(0, int(max_absent))
    except ValueError:
        return "Invalid data for calculation"


with requests.Session() as session:
    session.get(url, headers=headers)
    response = session.post(url, data=payload, headers=headers)
    all_data = []

    if response.status_code == 200:
        print("Login successful\n Fetching attendance data...\n")
        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find('tbody').find_all('tr')
        extracted_data = []

        for row in rows:
            course_code = row.find('td').text.strip()
            course_name = row.find_all('td')[1].text.strip()
            attendance_url = row.find_all('td')[4].find('a').get('href')
            attendance_button = row.find('button', class_='cn-attendanceclr')
            attendance_value = attendance_button.text.strip().split()[0] if attendance_button else None

            extracted_data.append({
                'course_code': course_code,
                'course_name': course_name,
                'attendance': attendance_value,
                'attendance_url': "https://parents.msrit.edu/newparents/" + attendance_url
            })

        # Fetch attendance details for each course
        for data in extracted_data:
            attendance_response = session.get(data['attendance_url'], headers=headers)
            attendance_soup = BeautifulSoup(attendance_response.content, 'html.parser')
            status_card = attendance_soup.find('div', class_='cn-att-stat')

            attendance_stats = {}
            if status_card:
                labels = status_card.find_all('span', class_='uk-label')
                for label in labels:
                    text = label.text.strip()
                    if '[' in text:
                        category, count = text.split('[')
                        count = count.strip(']')
                        attendance_stats[category.strip().lower()] = count
                # Calculate classes can be missed
                can_miss_more = calculate_classes(
                    attendance_stats.get('absent', 0),
                    attendance_stats.get('present', 0),
                    attendance_stats.get('still to go', 0)
                )
                attendance_stats['can_miss_more'] = can_miss_more
                print(f"{data['course_name']} ({data['course_code']}) - Attendance: {data['attendance']}")
                print(f"Present: {attendance_stats.get('present', 'N/A')}")
                print(f"Absent: {attendance_stats.get('absent', 'N/A')}")
                print(f"Still to go: {attendance_stats.get('still to go', 'N/A')}")
                print(f"Classes you can still miss: {can_miss_more}\n")
            else:
                print(f"No attendance data found for course {data['course_code']}.")

            all_data.append({
                'course_code': data['course_code'],
                'course_name': data['course_name'],
                'attendance_details': attendance_stats
            })

        # Save to JSON file
        with open('attendance_data.json', 'w') as json_file:
            json.dump(all_data, json_file, indent=4)
    else:
        print("Login failed")
