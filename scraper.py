import requests
from bs4 import BeautifulSoup

URL='https://en.wikipedia.org/wiki/History_of_Mexico'


def get_citations_needed_count(url):
  URL = url
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  citations = soup.find_all(class_='noprint Inline-Template Template-Fact')
  print(len(citations))
  return len(citations)

def get_citations_needed_report(url):
  URL = url
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  the_num_of_p = get_citations_needed_count(URL)
  
  for x in range(the_num_of_p):
    citations = soup.find_all(class_='Template-Fact')
    p = citations[x].parent.text.strip()
    print("\n","*"*100,"\n",p,"\n","*"*100,"\n")
  return p


get_citations_needed_count(URL)
get_citations_needed_report(URL)