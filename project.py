import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
from colorama import Fore,Back,Style

startTime=time.time()

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
counter=0
titles=[]
companies=[]
locations=[]

soup = BeautifulSoup(page.content,'html.parser')

results=soup.find(id='ResultsContainer')

job_elements = results.find_all("div",class_='card-content')

# python_jobs= results.find_all(
#     'h2', string=lambda text:'python' in text.lower()
# )

# python_job_elements = [
#     h2_element.parent.parent.parent for h2_element in python_jobs 
# ]

for job_element in job_elements:
    title_element = job_element.find('h2',class_='title')
    company_element = job_element.find('h3',class_='company')
    location_element = job_element.find('p',class_='location')
    titles.append(title_element.text.strip())
    companies.append(company_element.text.strip())
    locations.append(location_element.text.strip())
    counter+=1

    # print()
    # print(title_element.text.strip())
    # print(company_element.text.strip())
    # print(location_element.text.strip())
    # print()
    # print()


# Open the excel file in write mode
file = open('project_csv.csv', 'w')
# Create a csv writer object
file = csv.writer(file)
# Write the header row
file.writerow(['Job_Title', 'Company', 'Location'])
# Loop through the records and write them to the file
for i in range(counter):
    title = titles[i]
    company = companies[i]
    location = locations[i]
    file.writerow([title, company, location])


endTime=time.time()

turnAroundTime=endTime-startTime
print('\n\n')
print(f'Turnaround Time in '+Fore.GREEN+'regular'+Fore.WHITE+f' mode: {Fore.LIGHTBLUE_EX}{turnAroundTime*1000} ms{Fore.WHITE}')