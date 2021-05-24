import timing
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
import math
import numpy as np

DRIVER_PATH = "C:\\Users\\staya\\chromedriver"
BASE_URL = 'https://raleigh.craigslist.org'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

QUERY = '' #input what keyword you want to filter by
dates = []
post = []
posts = ()
soup = ()
find_all = []
data = []

def outputEntries(posts):
    for i, post in enumerate(posts):
        titleDiv = post.find('a', class_='result-title')
        postTitle = titleDiv.get_text()
        postURL = titleDiv.get('href')
        postDate = post.find('time', title_=[]).get_text()
        postTimeText = post.find('time').get('datetime')
        postTime = datetime.strptime(postTimeText, '%Y-%m-%d %H:%M')
        elapsedMinutes = math.ceil((datetime.now() - postTime).total_seconds() / 60)
        
        print(f'{i + 1}: {elapsedMinutes}:  {postDate}:   {postTitle}:   {postURL}')
        
        #n = int(str(totalPosts))
        #for item in range(0, n):
            #calculations = (elapsedMinutes)
            #list.append(calculations)
        #array_rEM = arr.array('f', rounded_EM)
        #sorted_array_rEM = sorted(array_rEM)
        
        #for datetime in range(len(posts)):
            #timestamp = datetime.strptime([datetime], '%Y-%m-%d %H:%M:%S')
            #dates.append(timestamp)

        #dates.sort(key=lambda date: datetime.strptime(date, "%d-%b-%y"))
        

def stepthroughpages(posts, pageLink):
    driver.get(BASE_URL + pageLink)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    nextButton = soup.find('a', class_='next')
    posts.extend(soup.find_all('li', 'result-row'))


    if nextButton is None: return posts
    return stepthroughpages(posts, nextButton.get('href'))

totalPosts = stepthroughpages([], '/search/tch')
totalPosts = [post for post in totalPosts if QUERY in post.find('a', class_='result-title').get_text().lower()]


print(f'{len(totalPosts)} results containing "{QUERY}"')
outputEntries(totalPosts)


driver.quit()




# .extend function allows me to create a big ass list by adding list elements to already existing li elements
#debug process
#tried disabling terminal.integrated.inheritEnv in settings. Tried an empty print statement at the end. Tried starting without debugging. Tried exit(). Tried running in terminal after exit(). Tried running selected text. Tried running active file. 
#issue resolved: s in StepThroughPages was not capitalized. Update: Disregard. Still flagged as invalid syntax. Tried assigning consistent lowercase, didn't work.
#Issue actually resolved: The error originated from a missing closed parenthesis on line 21. This flagged my next line as invalid syntax when the problem originated previously. Thank you StackOverFlow.
#Now I need to define posts
#Works now?????? Tuple issue resolved with find_all function in line 21. I changed the input to result-row instead of result-title, as well as adding line 30 in and defining find_all with an empty list with square brackets. Idk wtf happened but no errors.
#For enumerate, you can set the number you want to start at by adding it into the input:
    # enumerate(totalPosts)  would start at zero. However, if you were to add more to the input, enumerate(totalPosts, 1), this would avoid starting at zero because now I can manually set the list to start at any index value that I desire.
    
    #PDList.sort(key = lambda date: datetime.strptime(date, '%b %d'))
#def postdate(posts, pageLink):
    #driver.get(BASE_URL + pageLink)
    #soup = BeautifulSoup(driver.page_source, 'html.parser')
    #nextButton = soup.find('a', class_='next')
    #posts.extend(soup.find_all('li', 'result-date'))

    #if nextButton is None: return dates
    #return postdate(dates, nextButton.get('href'))

#totalPosts = stepthroughpages([], '/search/tch'), postdate([], '/search/tch')
#    print(str(i) + '.  ' + post.find('a', class_='result-title').get_text() + '  ' + 'Post Date:  ' + post.find('time', class_='result-date').get_text())
#   totalPosts = [post for post in totalPosts if 'software' in post.find('a', class_='result-title').get_text()]  <- is worthless because the filter is case-sensitive to the input, so I will not receive an output if there aren't any 'software' titles on the page in question. Need a more general filter to get rid of unrelated shit, however filter is almost pointless as it is. Will see about implementation.
#   ^update: Can use an if loop to convert the input to mulitple variations in upper/lowercase to account for variability in the lists being parsed. Can also set the input to a general variable that can be changed from the top of the code or even an input box from the frontend to customize the search to specific keywords, while still utlizing the if loop to account for spelling.
# list = []
        #for i in elapsedMinutes:
               # list.append(i)


