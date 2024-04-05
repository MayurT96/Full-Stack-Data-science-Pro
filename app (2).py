import requests # type: ignore
from bs4 import BeautifulSoup

def scrape_youtube():
    url = "https://www.youtube.com/results?search_query=tutorials"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    youtube_data = []

    for video in soup.find_all("a", class_="yt-simple-endpoint style-scope", href=True):
        if "watch?v=" in video["href"]:
            title = video.find("span", class_="yt-simple-endpoint style-scope").text
            url = f"https://www.youtube.com{video['href']}"
            youtube_data.append((title, url))

    return youtube_data