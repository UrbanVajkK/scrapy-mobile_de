from scrapy import Spider
from scrapy import Selector
from scrapy.http.request import Request
from mobile_de.items import MobileDeItem
import pickle as pickle
import smtplib


from_email = ["urbankrisztianvajk@gmail.com"]



class Mobile_deSpider(Spider):
    start_urls = [
        "http://suchen.mobile.de/auto/audi-a4-diesel-limousine.html?useCase=ChangeSortOrder&defaultOrder=DESCENDING&isSearchRequest=true&__lp=3&scopeId=C&sortOption.sortBy=specifics.mileage&makeModelVariant1.makeId=1900&makeModelVariant1.modelId=9&makeModelVariant1.searchInFreetext=false&makeModelVariant2.searchInFreetext=false&makeModelVariant3.searchInFreetext=false&minPowerAsArray=73&minPowerAsArray=KW&maxPowerAsArray=96&maxPowerAsArray=KW&fuels=DIESEL&minFirstRegistrationDate=2004-01-01&maxPrice=13001&ambitCountry=DE&negativeFeatures=EXPORT&maxMileage=125000&categories=Limousine&lang=de&sortPath=creationTime"
    ]
    allowed_domains = ["mobile.de"]


    def parse(self, response, url):
        hxs = Selector.xpath(response)
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

            yield items

        #items_db = pickle.load(open("mobile_de.idx", "rb"))

        # for item in items:
        #     if item["id"] not in items_db:
        #         msg = MIMEText(item["URL"])
        #         msg[
        #             'Subject'] = '[mobile_de alert] %(listEntryTitle)s | %(pricePrimaryCountryOfSale)s | %(firstRegistration)s | %(mileage)s | %(vehicleLocation)s' % item
        #         msg['From'] = from_email
        #         msg['To'] = ', '.join(to_emails)
        #         s = smtplib.SMTP('localhost')
        #         s.sendmail(from_email, to_emails, msg.as_string())
        #         s.quit()
        #
        #       items_db.update({item["id"]: True})
        #       print(items_db)
        #    pickle.dump(items_db, open("mobile_de.idx", "wb"))
        # return items_db

# get links
# df_meine_mobile = meine_mobile.get_links(df_meine_mobile)

# Mobile_deSpider(start_urls=urls)
#	for item in items:
#		yield item
