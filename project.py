import os
import csv
import time
import requests
import concurrent.futures
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from colorama import Fore,Back,Style



# [Initialize Variables]
URL = "https://realpython.github.io/fake-jobs/"
counter=0
state=0
titles=[]
companies=[]
locations=[]
pictures=[]



# [Scrape Tags From the Website]
def Scraping(state,keywords):
    
    counter=0
    
    search_elements=[]
    
    page = requests.get(URL)

    soup = BeautifulSoup(page.content,'html.parser')

    results=soup.find(id='ResultsContainer')

    if state == 0:
        search_elements = results.find_all("div",class_='card-content')
    else:
        engineer_jobs= results.find_all(
            'h2', string=lambda text:keywords in text.lower()
        )

        search_elements = [
            h2_element.parent.parent.parent for h2_element in engineer_jobs 
        ]

    for job_element in search_elements:
        title_element = job_element.find('h2',class_='title')
        company_element = job_element.find('h3',class_='company')
        location_element = job_element.find('p',class_='location')
        if title_element.text.strip().__contains__('/')==False:
            titles.append(title_element.text.strip())
            companies.append(company_element.text.strip())
            locations.append(location_element.text.strip())
            counter+=1

            if state==0:
                directory = "all"
                if not os.path.exists(directory):
                        os.makedirs(directory)
    
            else:
                directory = keywords
                if not os.path.exists(directory):
                    os.makedirs(directory)

    return counter



# [Write CSV Files and Photos in Directories]
def WritingFiles(count,state,search_title):
    
    # Open the excel file in write mode
    file = open('project_csv.csv', 'w')
    # Create a csv writer object
    file = csv.writer(file)
    # Write the header row
    file.writerow(['Job_Title', 'Company', 'Location'])
    # Loop through the records and write them to the file
    for i in range(count):
        title = titles[i]
        company = companies[i]
        location = locations[i]
        file.writerow([title, company, location])
        if state==0:
            path = os.path.join('all', title)
            if not os.path.exists(path):
                os.makedirs(path)
            # downloadPictures(titles[i],path)
        else:
           path = os.path.join(search_title, title)
           if not os.path.exists(path):
                os.makedirs(path)
           downloadPictures(titles[i],path)
            
                
    titles.clear()
        
        
              
# [Download Profile Pictures From Webserver]
def downloadPictures(name,directory):
    url = "https://files.realpython.com/media/real-python-logo-thumbnail.7f0db70c2ed2.jpg?__no_cf_polish=1"
    response = requests.get(url)
    # Create an img file
    with open(os.path.join(directory,f"{name}.jpg"), "wb") as f:
        f.write(response.content)
        
        
        
# [Create a Chart For Categories]
def CreateChart(data2,data3,data4,data5):
    x = ["Enginners", "Scientists", "Managers", "Developers"]
    y = [data2,data3,data4,data5]    
    colors=['#276BFF','#EC3A7B','#FFBC42','#1DB52C']
    plt.bar(x, y, color=colors)
    plt.xlabel('Amounts')
    plt.ylabel('Categories')
    plt.title('Summerizing Downloaded Photos Categories')
    plt.show()



# [Serialized Running]

# Start Timer
startTime1=time.time()
engineer_counter = Scraping(1,'engineer')
WritingFiles(engineer_counter,1,'engineer')
scientist_counter = Scraping(1,'scientist')
WritingFiles(scientist_counter,1,'scientist')
manager_counter = Scraping(1,'manager')
WritingFiles(manager_counter,1,'manager')
developer_counter = Scraping(1,'developer')
WritingFiles(developer_counter,1,'developer')
all_counter = Scraping(0,'')
WritingFiles(all_counter,0,'')
# Stop Timer
endTime1=time.time()



# [Multithreading Running]

# Start Timer
startTime2=time.time()
# Create a thread pool for concurrent runs of threads
threadPool=concurrent.futures.ThreadPoolExecutor(max_workers=10)
# Submit workers to threads pool
threadPool.submit(Scraping(1,'engineer'))
threadPool.submit(WritingFiles(engineer_counter,1,'engineer'))
threadPool.submit(Scraping(1,'scientist'))
threadPool.submit(WritingFiles(scientist_counter,1,'scientist'))
threadPool.submit(Scraping(1,'manager'))
threadPool.submit(WritingFiles(manager_counter,1,'manager'))
threadPool.submit(Scraping(1,'developer'))
threadPool.submit(WritingFiles(developer_counter,1,'developer'))
threadPool.submit(Scraping(0,''))
threadPool.submit(WritingFiles(all_counter,0,''))
threadPool.shutdown(wait=False)
# End Timer
endTime2=time.time()



# [Calculate Turnaround Times]
TT1=endTime1-startTime1
TT2=endTime2-startTime2



# [Printing Output]
print('\n\n')
print('----------------------------------------------------------------------------------------')
print(f'Turnaround Time in '+Fore.GREEN+'serialized'+Fore.WHITE+f' mode:          {Fore.LIGHTBLUE_EX}{round(TT1,8)*1000} ms{Fore.WHITE}')
print(f'Turnaround Time in '+Fore.YELLOW+'multithreading'+Fore.WHITE+f' mode:      {Fore.LIGHTBLUE_EX}{round(TT1,8)*1000} ms{Fore.WHITE}\n')
print(f'Performance improvement with multithreading:'+Fore.RED+f' {round(abs(TT2-TT1),8)*1000} ms'+Fore.WHITE)
print('----------------------------------------------------------------------------------------\n\n')

# [Showing Graph]
CreateChart(engineer_counter,scientist_counter,manager_counter,developer_counter)