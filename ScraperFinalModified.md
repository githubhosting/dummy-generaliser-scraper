Sure, here's the final README file explaining the approach and code structure:

# E-Commerce Product URL Scraper

This project is a web scraper designed to extract all product URLs from any given e-commerce website. The main goal is to fetch and filter out only the URLs that correspond to product pages, excluding other types of URLs such as social media links, login pages, or checkout pages.

## Approach

The approach taken in this project involves a combination of techniques:

1. **URL Fetching**: The code recursively fetches all URLs from a given root URL, traversing through the entire website's URL structure. This is done using the `fetch_urls` function, which follows links on each page and collects the URLs.

2. **Domain-based URL Filtering**: To ensure that the scraper only explores URLs within the target domain, the code implements a domain-based filtering mechanism. It uses the `urlparse` function to extract the domain part (netloc) of the URL and compares it with the domain part of the root URL. Only URLs belonging to the same domain as the root URL are processed.

3. **Cycle Detection**: To prevent infinite loops or cycles in the URL structure, the code maintains a set of visited URLs. If a URL has already been visited, it is skipped to avoid processing it again, effectively breaking any potential cycles.

4. **Page Content Analysis (Future Enhancement)**: While the current implementation relies solely on URL patterns, a potential enhancement would be to analyze the HTML content of each fetched page to look for elements or patterns commonly found on product pages, such as product titles, descriptions, prices, and add-to-cart buttons. This approach could improve the accuracy of identifying product pages, especially for websites with unconventional URL structures.

## Code Structure

The main script is located in `main.py`. Here's a brief overview of the key functions:

- `get_soup(url, use_selenium=False)`: This function fetches the HTML content of a given URL. It can use either requests (default) or Selenium (if `use_selenium` is True) to retrieve the page source.
- `extract_link_text(link)`: This function extracts the text associated with a link element. It handles cases where the link text is empty and tries to extract the title or content of the link.
- `fetch_urls(url, depth=0, visited=None, urls=None, use_selenium=False, root_url=None, count=0)`: This is the core function that recursively fetches URLs from a given root URL. It follows links on each page and collects the URLs, filtering out duplicates and URLs that don't belong to the target domain. The function implements cycle detection by maintaining a set of visited URLs.
- `filter_product_urls(df)`: This function takes a DataFrame containing fetched URLs and applies a regular expression pattern to filter out product URLs.
- `save_urls(urls, file_path)`: This function saves the extracted URLs to a CSV file.
- `save_to_json(urls, file_path)`: This function saves the extracted URLs to a JSON file.
- `main()`: This is the entry point of the script. It sets the root URL and calls the necessary functions to fetch, filter, and save the product URLs.

## Usage

To run the script, execute the `main.py` file. You can modify the `url1`, `url2`, and `url3` variables in the `main()` function to specify the root URL of the e-commerce website you want to scrape.

The script will recursively fetch all URLs from the specified root URL, filtering out URLs that don't belong to the target domain. It will then apply a regular expression pattern to identify and extract the product URLs. Finally, it will save the results to a CSV file (`csv_urls.csv`) and a JSON file (`json_urls.json`) in the `rawdata/myharvestfarms/` directory.

## Future Enhancements

Potential enhancements for this project include:

- Implementing page content analysis to improve product URL identification
- Utilizing parallel processing to improve performance
- Implementing caching and deduplication mechanisms
- Enhancing error handling and resilience
- Implementing logging and monitoring mechanisms

Feel free to explore these enhancements and contribute to the project's improvement.