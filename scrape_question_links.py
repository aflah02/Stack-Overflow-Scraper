import requests
from bs4 import BeautifulSoup

with open('cross_validated.txt', 'w') as f:
    for page_num in range(1, 50):
        link = f"https://stats.stackexchange.com/questions?tab=votes&page={page_num}"
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')

        ques = soup.find_all('h3', class_='s-post-summary--content-title')

        for q in ques:
            f.write(q.a['href'] + '\n')

