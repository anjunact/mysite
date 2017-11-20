from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class Command(BaseCommand):
    def getData(self):
        url='http://www.xicidaili.com'
        driver = webdriver.PhantomJS()
        driver.get(url)
        # elem = driver.find_element_by_id('ip_list')
        # print(elem)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        trs = soup.find(id="ip_list").find_all('tr')
        for tr in trs:
            tds =tr.find_all("td")
           
            i =0 ;
            for td in tds:
                if i==1 :
                    print(td)
                if i==2:
                    print(td)
                i=i+1
        
 
    def handle(self, *args, **options):
        self.getData()