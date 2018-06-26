import requests
import selenium
from bs4 import BeautifulSoup

r = requests.get("https://delhi.craigslist.co.in/d/accounting-finance/search/acc")
soup = BeautifulSoup(r.content, 'html.parser')


def getDescription(input):
    r1 = requests.get(input)
    soup1 = BeautifulSoup(r1.content, 'html.parser')
    return soup1.find('section', {"id": "postingbody"}).text
i=1
nested_dict={}
for result in soup.findAll('p'):
    my_dict={}
    my_dict['title']=result.find('a', {"result-title"}).text
    # print "Title      : " + my_list[-1]

    my_dict['description']=getDescription(result.find('a')['href'])
    # print "Description: " + my_list[-1]
    my_dict['date']=result.find('time', {"result-date"}).text
    # print "Date       : " + my_list[-1]
    # my_list.append(result.find('span', {"result-hood"}).text)
    if result.find('span', {"result-hood"}):
        my_dict['location']=result.find('span', {"result-hood"}).text

        # print "Location: " + my_list[-1]
    else:
        my_dict['location']='Not Specified'
        # print "Location: Not Specified"
    print my_dict
    print("___________________________________________________")

    nested_dict[i]=my_dict
    i+=1
print nested_dict