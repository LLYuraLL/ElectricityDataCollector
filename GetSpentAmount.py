from __future__ import unicode_literals
import pandas as pd
from twill.commands import *
from twill import browser
import os
import html5lib
from datetime import date
from os.path import exists as file_exists
import random
from bs4 import BeautifulSoup
from selenium import webdriver
# Get the current working directory
#cwd = os.getcwd()
# Print the current working directory
#print("Current working directory: {0}".format(cwd))
def main(StartY,StartM,StartD,EndY,EndM,EndD):    
    #StartY = input('Enter starting year(4 digits): ')
    #StartM = input('Enter starting month(2 digits): ')
    #StartD = input('Enter starting day(2 digits): ')
    #EndY = input('Enter ending year(4 digits): ')
    #EndM = input('Enter ending month(2 digits): ')
    #EndD = input('Enter ending day(2 digits): ')
    url = 'https://mitstromlinet.stromlinet.dk/forbrug.php'
    if not(StartY == EndY and StartM == EndM and StartD == EndD):
        browser.go(url)
        #browser.showforms()
        login = 68760
        password = 'fq94mmxQMvT7'
        formvalue('1', 'username', str(login))
        #browser.showforms()
        formvalue('1','password', password)
        #browser.showforms()
        submit()
        go('https://mitstromlinet.stromlinet.dk/forbrug.php')
        formvalue('1', 'typeddl', "Time")
        submit()
        os.chdir('/Users/upsem/Documents/WebScrapperPY/Stromlinet_Spent')
        while int(StartY) <= int(EndY):
            while int(StartM) <= 12:
                if int(StartM) == 12:
                    NumOfDays = (date(int(StartY) + 1,1,1)-date(int(StartY),int(StartM),1)).days
                else:
                    NumOfDays = (date(int(StartY),int(StartM) + 1,1)-date(int(StartY),int(StartM),1)).days
                while int(StartD) <= NumOfDays:
                    if file_exists('C:\\Users\\upsem\\Documents\\WebScrapperPY\\Stromlinet_Prices\\SpentOn' + str(StartY + '-' + StartM + '-' + StartD) + '.csv'):
                        StartD = str(int(StartD) + 1).zfill(2)
                        continue
                    else:
                        formvalue('1', 'typeddl', "Time")
                        submit()
                        formvalue('1', 'yeardll', str(StartY))
                        submit()
                        sleep(random.randint(2,4))
                        formvalue('1', 'monthdll', str(StartY + '-' + StartM))
                        submit()
                        sleep(random.randint(2,4))
                        try:
                            formvalue('1', 'daysddl', str(StartY + '-' + StartM + '-' + StartD))
                            submit()
                            sleep(random.randint(2,4))
                            print('Saving '+ '\'PriceOn-' + str(StartY + '-' + StartM + '-' + StartD)+'\'')
                            save_html('PriceOn-' + str(StartY + '-' + StartM + '-' + StartD))
                            sleep(8+random.randint(1,3))
                            html = open('PriceOn-' + str(StartY + '-' + StartM + '-' + StartD), 'r')
                            df_list = pd.read_html(html)
                            df = df_list[-1]
                            df.to_csv('SpentOn'+ str(StartY + '-' + StartM + '-' + StartD) +'.csv')
                        except:
                            print("There is no day " + str(StartY + '-' + StartM + '-' + StartD) + " in list")
                        #print(StartY + '-' + StartM + '-' + StartD)
                    if StartD == EndD:
                        if StartM == EndM:
                            if StartY == EndY:
                                break
                    StartD = str(int(StartD) + 1).zfill(2)
                if StartD == EndD:
                        if StartM == EndM:
                            if StartY == EndY:
                                break
                if int(StartM) == 12:
                    StartD = '01'
                    StartM = '01'
                    StartY = str(int(StartY) + 1)
                else:
                    StartD = '01'
                    StartM = str(int(StartM) + 1).zfill(2)
                if StartM == EndM:
                    break
            if StartD == EndD:
                        if StartM == EndM:
                            if StartY == EndY:
                                break
    print('Work finished')
'''
save_html('Test_Of_Stromlinet-' + str(StartY + '-' + StartM + '-' + StartD))
html = open('Test_Of_Stromlinet-' + str(StartY + '-' + StartM + '-' + StartD), 'r')
doc_for_soup = str('C:/Users/upsem/Documents/WebScrapperPY/est_Of_Stromlinet-' + str(StartY + '-' + StartM + '-' + StartD))
soup = BeautifulSoup(doc_for_soup, 'html5lib')
df_list = pd.read_html(html)
df = df_list[-1]
df.to_csv('Test_Of_Stromlinet_CSV'+ str(StartY + '-' + StartM + '-' + StartD) +'.csv')
'''
"""
browser.go('https://www.nordpoolgroup.com/en/Market-data1/Dayahead/Area-Prices/DK/Hourly/?view=table')
sleep(5)
browser.showforms()
formvalue('1', 'query', '01 OCT 2022')
save_html('NordPool_HTML')
browser.showforms()
#show()
#showlinks()

# initiate the browser. It will open the url, 
# and we can access all its content, and make actions on it. 
browser = webdriver.Firefox()
# the page test.html is changing constantly its content by receiving sockets, etc. 
#So we need to save its "status" when we decide for further retrieval)
browser.get(url)
# wait until we want to save the content (this could be a buttonUI action, etc.):
raw_input("Press to print web page")  
# save the html rendered content in that moment: 
html_source = browser.page_source
# display to check: 
print (html_source)
"""
