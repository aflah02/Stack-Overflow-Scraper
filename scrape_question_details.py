import requests
from bs4 import BeautifulSoup
import pandas as pd

with open('cross_validated.txt', 'r') as f:
    links = f.readlines()

BASE_URL = "https://stats.stackexchange.com/"

list_results = []

for sublink in links:
    link = BASE_URL + sublink.strip()
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('a', class_='question-hyperlink').text
    question_body = " ".join(soup.find('div', class_='s-prose js-post-body').text.replace('\n', ' ').replace('\t', ' ').strip().split())
    list_results.append([link, title, question_body])

df = pd.DataFrame(list_results)
df.columns = ['link', 'title', 'question_body']
df.to_csv('cross_validated_details.csv', index=False)
