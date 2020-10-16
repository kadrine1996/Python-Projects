import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.ca/jobs/search/?q=Programmers&where=Vaughan__2C-ON&intcid=skr_navigation_nhpso_searchMain'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')

#For specific developer jobs
developer_jobs = results.find_all("h2", string=lambda t: "developer" in t.lower())
for d_jobs in developer_jobs:
    link = d_jobs.find('a')['href']
    print("\n")
    print(d_jobs.text.strip())
    print(f"Apply here: {link}\n")
    


# All jobs from the monster page
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    #link_elems = results.find_all("h2")
    #for link_elem in link_elems:
        #links = link_elem.find('a')['href']
    print()