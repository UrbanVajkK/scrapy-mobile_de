
import scrapy
from scrapy import Spider
from scrapy import Selector
from scrapy.http.request import Request
from mobile_de.items import MobileDeItem
from spread_mobile import SpreadMobile
from mobile_de_spider import Mobile_deSpider
import bs4

# grab data from spread
spread_mobile = SpreadMobile()
df_mobile = spread_mobile.df_from_worksheet(spread_mobile.connect_to_spread())

# get links
df_mobile = spread_mobile.get_links(df_mobile)
link = df_mobile.iloc[0]
print(link)

#  parse got link
meineSpinne = Mobile_deSpider(link)
meine_Antwort = meineSpinne.parse(meineSpinne.start_requests())
print(meine_Antwort)

from scrapy.selector import Selector
from scrapy.http import HtmlResponse

response = HtmlResponse(url=link)



class Myspider(Spider):
    start_urls = [link]
    def __init__(self, name='Spinne'):
        self.name = name

    def parse(self, response, **kwargs):

        hxs = Selector.xpath(self, response).getall()
        next_page = hxs.select('//a[@class="pg-btn page-next"]/@href').extract()
        ads = hxs.select('//div[@class="listEntry normalAd "]')

        items = []

        for ad in ads:
            item = MobileDeItem()
            item["id"] = ad.select('div[@class="parkCompare"]/input[@name="parkAndCompare"]/@value').extract()[0]
            item["URL"] = ad.select(
                'div[@class="vehicleDetails "]/div[@class="listEntryTitle"]/a[@class="infoLink detailsViewLink"]/@href').extract()[
                0].split("?")[0]
            item["listEntryTitle"] = ad.select(
                'div[@class="vehicleDetails "]/div[@class="listEntryTitle"]/a[@class="infoLink detailsViewLink"]/text()').extract()[
                0]
            item["vehicleLocation"] = ad.select(
                'div[@class="vehicleDetails "]/div[@class="descriptions"]/div[@class="vehicleLocation"]/text()').extract()[
                0].strip()
            item["pricePrimaryCountryOfSale"] = \
                ad.select('div[@class="vehicleDetails "]//div[@class="pricePrimaryCountryOfSale"]/text()').extract()[
                    0].strip()
            item["mileage"] = ad.select('div[@class="vehicleDetails "]//div[@class="mileage"]/text()').extract()[
                0].strip()
            item["firstRegistration"] = \
                ad.select('div[@class="vehicleDetails "]//div[@class="firstRegistration"]/text()').extract()[0].strip()
            item["vendorType"] = ad.select('div[@class="vehicleDetails "]//div[@class="vendorType"]/text()').extract()[
                0].strip()
            items.append(item)

        print(items)



Spydy = Myspider(name='szkrépi')
parsed = Spydy.parse(Spydy.start_requests())
print(parsed)




Spydy.start_requests(callable())
hxs = Selector.xpath(self=None , query=link).getall()
next_page = hxs.select('//a[@class="pg-btn page-next"]/@href').extract()
ads = hxs.select('//div[@class="listEntry normalAd "]')

items = []

for ad in ads:
    item = MobileDeItem()
    item["id"] = ad.select('div[@class="parkCompare"]/input[@name="parkAndCompare"]/@value').extract()[0]
    item["URL"] = ad.select(
        'div[@class="vehicleDetails "]/div[@class="listEntryTitle"]/a[@class="infoLink detailsViewLink"]/@href').extract()[
        0].split("?")[0]
    item["listEntryTitle"] = ad.select(
        'div[@class="vehicleDetails "]/div[@class="listEntryTitle"]/a[@class="infoLink detailsViewLink"]/text()').extract()[
        0]
    item["vehicleLocation"] = ad.select(
        'div[@class="vehicleDetails "]/div[@class="descriptions"]/div[@class="vehicleLocation"]/text()').extract()[
        0].strip()
    item["pricePrimaryCountryOfSale"] = \
        ad.select('div[@class="vehicleDetails "]//div[@class="pricePrimaryCountryOfSale"]/text()').extract()[
            0].strip()
    item["mileage"] = ad.select('div[@class="vehicleDetails "]//div[@class="mileage"]/text()').extract()[
        0].strip()
    item["firstRegistration"] = \
        ad.select('div[@class="vehicleDetails "]//div[@class="firstRegistration"]/text()').extract()[0].strip()
    item["vendorType"] = ad.select('div[@class="vehicleDetails "]//div[@class="vendorType"]/text()').extract()[
        0].strip()
    items.append(item)

print(items)
