import random
from selenium.webdriver.common.proxy import ProxyType 
from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.db import connection
from main.models import t_ip


class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('check',nargs='+', type=str)

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
            tip = t_ip()
            for td in tds:
                if i==1 :
                    tip.ip = td.text
                if i==2:
                    tip.port = int(td.text)
                i=i+1
            # print(tip)
            if tip.ip !=None and tip.port != None:
                tip.save()
            
    def check(self):
        driver = webdriver.PhantomJS()      
        proxy=webdriver.Proxy()
        proxy.proxy_type= ProxyType.MANUAL
        proxy.http_proxy='1.9.171.51:800'             
        ips =self.allip()
        i = random.randint(0,len(ips))
        endport = ips[i]
        proxy.http_proxy = endport.ip+':'+endport.port
        driver.get("http://www.baidu.com")
        soup = BeautifulSoup(driver.page_source, 'lxml')
        title = soup.find_all('title')  
        print(title)
        
    def allip(self):
        return t_ip.objects.all()
    def handle(self, *args, **options):
        check = options['check']
        if(len(check)>0 and check[0]=='check'):  
                
            self.check()
        else:
            cursor= connection.cursor()
            cursor.execute("truncate table main_t_ip")
            self.getData()