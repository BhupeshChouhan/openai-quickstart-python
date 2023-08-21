from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json


def search_and_extract_links(query):
    # Set up the web driver in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # This line makes the browser run in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the webpage
    url = f"https://duckduckgo.com/?q={query}&ia=web"  # Replace with the URL you want to scrape
    driver.get(url)

    # Retrieve the entire webpage source
    page_source = driver.page_source

    # Close the web driver
    driver.quit()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the section with the specified attributes
    target_section = soup.find("section", attrs={"data-testid": "mainline", "data-area": "mainline"})

    if target_section:
        # Extract and store links with associated text within the target section
        link_data = []

        for link in target_section.find_all("a", href=True):
            href = link["href"]
            if href.startswith("https"):
                span = link.find_next("span")
                text = span.get_text() if span else "No associated text"
                link_data.append({"link": href, "text": text})

        # Create a dictionary to store the result
        output = {
            "link_data": link_data
        }

    output = json.dumps(output, indent=4)

    return output


search_query = input("Enter the search query: ")
output = search_and_extract_links(search_query)

#new change

print(output)
