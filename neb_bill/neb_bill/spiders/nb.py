import scrapy
from selenium import webdriver
from scrapy import Selector
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
PROXY = '51.81.80.170:8080'
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",
}
webdriver.DesiredCapabilities.CHROME['acceptSslCerts']=True
import time
import csv
path = R"E:\Desktop\nebraska\chromedriver.exe"
li = [0,25,50,75,100,125,150,175,200,225,250,275,300,325]


a_list = []
b_list = []
class NbSpider(scrapy.Spider):
    name = 'nb'
    # allowed_domains = ['http://nebraskalegislature.gov/bills/search_by_keyword.php?start=0']
    start_urls = ['http://www.google.com/']

    def parse(self, response):
        try:
            driver = webdriver.Chrome(path)
            for i in li:
                driver.get("http://nebraskalegislature.gov/bills/search_by_keyword.php?start="+str(i)+"&keyword=passed")
                sel = Selector(text=driver.page_source)
                bill = sel.xpath('//div[@class="card"]/div[@class="card-header leg-header"]/text()').getall()
                link = sel.xpath('//div[@class="card"]//div[@class="card-body"]/ul/li/a/@href').getall()
                for l in link:
                    b_list.append(l)
                for a in bill:
                    a_list.append(a)
            with open(R"E:\Desktop\nebraska\out_1.csv", "w", newline='', encoding='utf-8') as myfile:
                csv_writer = csv.writer(myfile,delimiter=",")
                for a,c in zip(a_list,b_list):
                    csv_writer.writerow([a,c])
                myfile.close()

            print("%%%%%%",a_list)
            # print(len(b_list))
        except Exception as e:

            print("###################",e)



        pass
