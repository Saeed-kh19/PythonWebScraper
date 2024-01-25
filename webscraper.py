import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

job_elems = results.find_all("div", class_="card-content")

for job_elem in job_elems:
    title_elem = job_elem.find("h2", class_="title is-5")
    company_elem = job_elem.find("h3", class_="subtitle is-6 company")
    location_elem = job_elem.find("p", class_="location")
    date_elem = job_elem.find("p", class_="posted")
    link_elem = job_elem.find("a", href=True)

    if None in (title_elem, company_elem, location_elem, date_elem, link_elem):
        continue

    print(f"{title_elem.text.strip()} at {company_elem.text.strip()}")
    print(f"{location_elem.text.strip()} | {date_elem.text.strip()}")
    print(f"Apply here: {link_elem['href']}\n")