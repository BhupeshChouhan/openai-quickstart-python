import requests
from bs4 import BeautifulSoup
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Navigate to the webpage
url = "https://en.wikipedia.org/wiki/Main_Page"  # Replace with the URL you want to scrape


def search_and_extract_links(query):

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # This line makes the browser run in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    search_url = f"https://duckduckgo.com/?q={query}&ia=web"  # Replace with the appropriate search URL
    driver.get(search_url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Retrieve the entire webpage source
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        # print(page_source)
        print(soup)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            link_elements = soup.find_all("div", class_='module--carousel__body__title')

            links = []
            for link_element in link_elements:
                link = link_element["href"]
                if not link.startswith("http"):  # Skip relative URLs
                    continue
                if "ad" not in link.lower():
                    links.append(link)
                if len(links) >= 2:
                    break

            return links
        else:
            print("Failed to fetch search results.")
            return []

    # Close the web driver
    driver.quit()


search_query = input("Enter the search query: ")
search_results = search_and_extract_links(search_query)

output = {
    "search_query": search_query,
    "links": search_results[:2]
}

print(output)
