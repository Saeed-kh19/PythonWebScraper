import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')

results=soup.find(id='ResultsContainer')

job_elements = results.find_all("div",class_='card-content')

python_jobs= results.find_all(
    'h2', string=lambda text:'python' in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs 
]

for job_element in python_job_elements:
    title_element = job_element.find('h2',class_='title')
    company_element = job_element.find('h3',class_='company')
    location_element = job_element.find('p',class_='location')


    print()
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    print()

    # links = job_element.find_all("a")
    # for link in links:
    #     link_url = link['href']
    #     print(f'Apply here: {link_url} \n')

    # for job_element in python_job_elements:
    #     link_url = job_element.find_all("a")[1]["href"]
    #     print(f"Apply here: {link_url}\n")



# Import csv module
import csv

# Open the excel file in write mode
file = open('project_csv.xlsx', 'w')

# Create a csv writer object
file = csv.writer(file)

# Write the header row
file.writerow(['Name', 'Age', 'Enrollment Number'])

# Take user input for the number of records
n = int(input('How many records you want to insert: '))

# Loop through the records and write them to the file
for i in range(n):
    name = input(f' {i+1}. Enter name: ')
    age = input(f' {i+1}. Enter age: ')
    enroll = input(f' {i+1}. Enter Enrollment number: ')
    file.writerow([name, age, enroll])

# Close the file
file.close()

# Print a success message
print('All records inserted successfully !')

