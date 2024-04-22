To tackle the task of extracting only the product URLs from an e-commerce website, we can follow a combination of techniques. Here's a high-level approach you could consider:

1. **Initial Filtering**: Before fetching the URLs, you can employ some heuristics to filter out unwanted URLs that are less likely to be product pages. For example, you could exclude URLs containing certain keywords like "login," "cart," "checkout," etc.

2. **URL Pattern Analysis**: Analyze the URL patterns of known product pages from the website. Often, product URLs follow a specific structure or contain certain keywords or patterns. You can then use regular expressions or string matching to identify URLs that match these patterns.

3. **Content Analysis**: Once you have fetched the URLs, you can analyze the content of each page to determine if it's a product page or not. This can be done by looking for specific HTML elements or text patterns commonly found on product pages, such as product titles, descriptions, prices, add-to-cart buttons, etc.

4. **Machine Learning Approach**: If the above techniques are not sufficient, you could consider using a machine learning model to classify the URLs or pages as product pages or non-product pages. This would involve:
   - Collecting a labeled dataset of product and non-product pages from the target website (or similar websites).
   - Extracting relevant features from the URLs, HTML content, or both.
   - Training a binary classifier (e.g., logistic regression, decision trees, or neural networks) on the labeled data.
   - Using the trained model to predict whether a new URL or page is a product page or not.

5. **Recursive Filtering**: Since product pages often link to other product pages, you could recursively follow these links and apply the filtering techniques mentioned above to identify additional product URLs.

Here's a high-level pseudocode combining some of these techniques:

```python
def fetch_product_urls(url, depth=0, max_depth=2, visited=None, product_urls=None, use_selenium=False):
    if visited is None:
        visited = set()
    if product_urls is None:
        product_urls = []

    if depth > max_depth or url in visited:
        return product_urls

    visited.add(url)
    soup = get_soup(url, use_selenium)
    if not soup:
        return product_urls

    # Initial filtering based on URL patterns
    if is_potential_product_url(url):
        # Analyze content to determine if it's a product page
        if is_product_page(soup):
            product_urls.append(url)

        # Recursively follow links on the page
        for link in soup.find_all("a", href=True):
            href = urljoin(url, link["href"])
            product_urls = fetch_product_urls(href, depth + 1, max_depth, visited, product_urls, use_selenium)

    return product_urls
```

In this pseudocode, the `is_potential_product_url` function applies the initial URL filtering heuristics, and the `is_product_page` function analyzes the page content to determine if it's a product page or not. These functions can be implemented using regular expressions, string matching, or machine learning techniques, depending on your requirements.

Note that this is a high-level approach, and you might need to adapt and refine it based on the specific characteristics of the e-commerce website you're targeting and the quality of the results you obtain.