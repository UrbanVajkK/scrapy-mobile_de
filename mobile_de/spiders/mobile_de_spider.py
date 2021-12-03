from scrapy import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from mobile_de.items import MobileDeItem
import pickle as pickle
import smtplib
from email.mime.text import MIMEText

from spread_mobile import SpreadMobile

from_email = ["urbankrisztianvajk@gmail.com"]
to_emails = ["urbankrisztianvajk@gmail.com"]


class Mobile_deSpider(BaseSpider):

    def __init__(self, name = "mobile_de", allowed_domains = ["mobile.de"], start_urls=None):
        if start_urls is None:
            start_urls = [
                "http://suchen.mobile.de/auto/audi-a4-diesel-limousine.html?useCase=ChangeSortOrder&defaultOrder=DESCENDING&isSearchRequest=true&__lp=3&scopeId=C&sortOption.sortBy=specifics.mileage&makeModelVariant1.makeId=1900&makeModelVariant1.modelId=9&makeModelVariant1.searchInFreetext=false&makeModelVariant2.searchInFreetext=false&makeModelVariant3.searchInFreetext=false&minPowerAsArray=73&minPowerAsArray=KW&maxPowerAsArray=96&maxPowerAsArray=KW&fuels=DIESEL&minFirstRegistrationDate=2004-01-01&maxPrice=13001&ambitCountry=DE&negativeFeatures=EXPORT&maxMileage=125000&categories=Limousine&lang=de&sortPath=creationTime"
            ]

        self.name = name
        self.allowed_domains = allowed_domains
        self.start_urls = start_urls


    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        next_page = hxs.select('//a[@class="pg-btn page-next"]/@href').extract()
        if not not next_page:
            yield Request(next_page[0], self.parse)

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

        items_db = pickle.load(open("mobile_de.idx", "rb"))

        for item in items:
            if item["id"] not in items_db:
                msg = MIMEText(item["URL"])
                msg[
                    'Subject'] = '[mobile_de alert] %(listEntryTitle)s | %(pricePrimaryCountryOfSale)s | %(firstRegistration)s | %(mileage)s | %(vehicleLocation)s' % item
                msg['From'] = from_email
                msg['To'] = ', '.join(to_emails)
                s = smtplib.SMTP('localhost')
                s.sendmail(from_email, to_emails, msg.as_string())
                s.quit()

                items_db.update({item["id"]: True})

        pickle.dump(items_db, open("mobile_de.idx", "wb"))

meine_mobile = spread_mobile()
df_meine_mobile = meine_mobile.df_from_worksheet(meine_mobile.connect_to_spread())
df_meine_mobile.head(5)

# get links
df_meine_mobile = meine_mobile.get_links(df_meine_mobile)

Mobile_deSpider(start_urls=urls)
#	for item in items:
#		yield item
