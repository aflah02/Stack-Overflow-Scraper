import requests
from bs4 import BeautifulSoup
import csv

with open('cross_validated.txt', 'r') as f:
    links = f.readlines()

BASE_URL = "https://stats.stackexchange.com/"

list_results = []

with open('cross_validated_details.csv', 'w', encoding='utf-8') as csvfile:
    fieldnames = ['link', 'title', 'question_body']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for sublink in links:
        try:
            link = BASE_URL + sublink.strip()
            page = requests.get(link)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find('a', class_='question-hyperlink').text
            question_body = " ".join(soup.find('div', class_='s-prose js-post-body').text.replace('\n', ' ').replace('\t', ' ').strip().split())
            list_results.append([link, title, question_body])
            print("At Link: " + link + " Title: " + title + " Question Body: " + question_body)
            writer.writerow({'link': link, 'title': title, 'question_body': question_body})
        except:
            print(f"{link} failed")
            continue

