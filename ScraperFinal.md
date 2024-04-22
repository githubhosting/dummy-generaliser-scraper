# E-Commerce Product URL Scraper

This project is a web scraper designed to extract product URLs from any given e-commerce website. The main goal is to
fetch and filter out only the URLs that correspond to product pages, excluding other types of URLs such as social media
links, login pages, or checkout pages.

## Approach

The approach taken in this project involves a combination of techniques:

1. **URL Fetching**: The code fetches all URLs from a given root URL up to a specified depth. This is done using a
   recursive function `fetch_urls` that follows links on each page and collects the URLs.

2. **URL Filtering**: To identify product URLs, the code applies a regular expression pattern to filter out URLs that
   match a specific structure. The current pattern (`r'https?://[^/]+/product/[^ ]+'`) looks for URLs containing
   the `/product/` segment, but this can be generalized to accommodate different URL structures used by various
   e-commerce websites.

3. **Page Content Analysis (Future Enhancement)**: While the current implementation relies solely on URL patterns, a
   potential enhancement would be to analyze the HTML content of each fetched page to look for elements or patterns
   commonly found on product pages, such as product titles, descriptions, prices, and add-to-cart buttons. This approach
   could improve the accuracy of identifying product pages, especially for websites with unconventional URL structures.

4. **Recursive URL Extraction**: Another potential enhancement is to implement recursive URL extraction. Since product
   pages often link to other product pages, the code could recursively follow these links and continue filtering and
   extracting product URLs until a certain depth or until no new product URLs are found.

## Code Structure

The main script is located in `main.py`. Here's a brief overview of the key functions:

- `get_soup(url, use_selenium=False)`: This function fetches the HTML content of a given URL. It can use either
  requests (default) or Selenium (if `use_selenium` is True) to retrieve the page source.
- `extract_link_text(link)`: This function extracts the text associated with a link element. It handles cases where the
  link text is empty and tries to extract the title or content of the link.
- `fetch_urls(url, depth=0, max_depth=2, visited=None, urls=None, use_selenium=False, root_url=None, count=0)`: This is
  the core function that recursively fetches URLs from a given root URL. It follows links on each page and collects the
  URLs, filtering out duplicates and URLs that don't start with the root URL.
- `filter_product_urls(df)`: This function takes a DataFrame containing fetched URLs and applies the regular expression
  pattern to filter out product URLs.
- `save_urls(urls, file_path)`: This function saves the extracted URLs to a CSV file.
- `save_to_json(urls, file_path)`: This function saves the extracted URLs to a JSON file.
- `main()`: This is the entry point of the script. It sets the root URL, maximum depth, and calls the necessary
  functions to fetch, filter, and save the product URLs.

## Usage

To run the script, execute the `main.py` file. You can modify the `url1`, `url2`, and `url3` variables in the `main()`
function to specify the root URL of the e-commerce website you want to scrape.

The script will fetch all URLs from the specified root URL up to the defined `max_depth`, filter out the product URLs
based on the regular expression pattern, and save the results to a CSV file (`csv_urls.csv`) and a JSON
file (`json_urls.json`) in the `rawdata/myharvestfarms/` directory.

## Future Enhancements

As mentioned in the Approach section, potential enhancements include:

- Generalizing the regular expression pattern to accommodate different URL structures
- Implementing page content analysis to improve product URL identification
- Implementing recursive URL extraction to follow links on product pages
- Utilizing parallel processing to improve performance
- Implementing caching and deduplication mechanisms
- Enhancing error handling and resilience
- Implementing logging and monitoring mechanisms

Feel free to explore these enhancements and contribute to the project's improvement.