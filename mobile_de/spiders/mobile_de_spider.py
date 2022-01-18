import scrapy


class MobileSpider(scrapy.Spider):
    name = "spider_Mobile_de"
    start_urls = [
        'https://www.zyte.com/blog/'
                    ]
    allowed_domains = ["mobile.de"]

    def parse(self, response):
        for ad in response.xpath('//div[@class="listEntry normalAd "]'):
            row = {'ad': ad.css('::text').get()}
            print(row)
            yield row


        # for ad in ads:
        #     item = MobileDeItem()
        #     item["id"] = ad.select('div[@class="parkCompare"]/input[@name="parkAndCompare"]/@value').extract()[0]
        #     item["URL"] = ad.select(
        #         'div[@class="vehicleDetails "]/div[@class="listEntryTitle"]/a[@class="infoLink detailsViewLink"]/@href').extract()[
        #         0].split("?")[0]
        #     item["listEntryTitle"] = ad.select(
        #         'div[@class="vehicleDetails "]/div[@class="listEntryTitle"]/a[@class="infoLink detailsViewLink"]/text()').extract()[
        #         0]
        #     item["vehicleLocation"] = ad.select(
        #         'div[@class="vehicleDetails "]/div[@class="descriptions"]/div[@class="vehicleLocation"]/text()').extract()[
        #         0].strip()
        #     item["pricePrimaryCountryOfSale"] = \
        #         ad.select('div[@class="vehicleDetails "]//div[@class="pricePrimaryCountryOfSale"]/text()').extract()[
        #             0].strip()
        #     item["mileage"] = ad.select('div[@class="vehicleDetails "]//div[@class="mileage"]/text()').extract()[
        #         0].strip()
        #     item["firstRegistration"] = \
        #         ad.select('div[@class="vehicleDetails "]//div[@class="firstRegistration"]/text()').extract()[0].strip()
        #     item["vendorType"] = ad.select('div[@class="vehicleDetails "]//div[@class="vendorType"]/text()').extract()[
        #         0].strip()
        #     items.append(item)
