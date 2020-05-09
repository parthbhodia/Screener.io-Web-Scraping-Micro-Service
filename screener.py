from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.keys
import time
from bs4 import BeautifulSoup
import pandas as pd

from tkintertable import Tk
from tkinter.filedialog import askopenfilename
from csv import reader 


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
def read_csv():    
    # read csv file as a list of lists
    with open(filename, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        print(list_of_rows)
#from secrets import username, password

#driver = webdriver.Chrome("C:\DRIVERS\chrome\chromedriver.exe")

class ScreenerBot():
    
    global profit_loss
    def __init__(self):
        self.driver = webdriver.Chrome("C:\DRIVERS\chrome\chromedriver.exe")

    def login(self,company_name):
        self.driver.get('https://www.screener.in/')

        sleep(2)
        
        try:
            enter_company_name = self.driver.find_element_by_xpath('//*[@id="content-area"]/div/div/div/div/input')
            enter_company_name.send_keys(company_name)
            sleep(2)
    
            enter_company_name.send_keys(Keys.ENTER)
            sleep(2)
            
            sales = self.driver.find_element_by_xpath('//*[@id="profit-loss"]/div[3]/table/tbody/tr[1]/td[1]/button')
            sales.send_keys(Keys.ENTER)
            
            sleep(2)
            
            expense = self.driver.find_element_by_xpath('//*[@id="profit-loss"]/div[3]/table/tbody/tr[3]/td[1]/button')
            expense.send_keys(Keys.ENTER)
            
            sleep(2)
            
    #        rows = len(self.driver.find_elements_by_xpath('//*[@id="profit-loss"]/div[3]/table/tbody/tr/td'))
    #        cols = len(self.driver.find_elements_by_xpath('//*[@id="profit-loss"]/div[3]/table/thead/tr/th'))
    #        print (rows)
    #        print(cols)
            
            
            page_source = self.driver.page_source
            
            
    #        soup = BeautifulSoup(page_source.content, 'html5lib')
    #        table = soup.find_all('table', attrs={'class':'class="data-table responsive-text-nowrap"'})
    #        print(table)
            
            data = pd.read_html(page_source)
            print(data[2])
            profit_loss = data[2].copy()
            profit_loss.to_excel('screener_sales_report_'+company_name+'.xls')
        except ValueError:
            print('Error')
            
#        soup = BeautifulSoup(page_source, 'lxml')
#        
#        table = soup.find_all('table', attrs={'class':'class="data-table responsive-text-nowrap"'})
#       
#        for row in soup('table')[3].findAll('tr'):
#            tds = row('td')
#            if not tds:
#                continue
#            print( u' '.join([cell.string for cell in tds if cell.string]))
#     reviews = []
#        reviews_selector = soup.find_all('div', class_='reviewSelector')
#        for review_selector in reviews_selector:
#            review_div = review_selector.find('div', class_='dyn_full_review')
#            if review_div is None:
#                review_div = review_selector.find('div', class_='basic_review')
#            review = review_div.find('div', class_='entry').find('p').get_text()
#            review = review.strip()
#            reviews.append(review)
#        for r in range(1,15):
#            for c in range(1,cols+1):
#                value = self.driver.find_element_by_xpath('//*[@id="profit-loss"]/div[3]/table/tbody/tr['+str(r)+']/td[' + str(c) +']').text       
#        value = driver.value
        
    def close(self):
        self.driver.quit()
#    
list_companies = ['TCS','TCL']

for i in list_companies:
    bot = ScreenerBot()
    bot.login(i)
    bot.close()