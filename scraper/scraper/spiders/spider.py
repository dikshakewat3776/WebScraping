import scrapy
import re

SPIDER_NAME = "necklaceSets"
MAIN_URL = "https://www.houseofindya.com"


class NecklaceSetsSpider(scrapy.Spider):
    name = SPIDER_NAME

    def start_requests(self):
        allowed_domains = [MAIN_URL]
        url = "{}/zyra/necklace-sets/cat".format(MAIN_URL)
        yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response, **kwargs):
    #     for n in response.css('div.catgName'):
    #         yield {
    #             'necklaceSetName': n.css('p::text').getall()
    #         }

    def parse(self, response, **kwargs):
        for i in response.css('div.catgList a').getall():
            # resp = {
            #     "necklaceSet": i.getall()
            # }
            try:
                necklaceSetName = re.search('title=\"(.+?)\"', i).group(1)
            except AttributeError:
                necklaceSetName = ''

            try:
                necklaceDescription = re.search('<p>(.+?)</p>', i).group(1)
            except AttributeError:
                necklaceDescription = ''

            try:
                necklaceImageLink = re.search('data-original=\"(.+?)\"', i).group(1)
            except AttributeError:
                necklaceImageLink = ''

            try:
                necklacePrice = re.search('<i class="fal fa-rupee-sign"></i>(.+?)"', i).group(1).split("<")[0]
            except AttributeError:
                necklacePrice = ''

            resp = {
                "necklaceSetName": necklaceSetName,
                "necklaceImageLink": necklaceImageLink,
                "necklaceDescription": necklaceDescription,
                "necklacePrice": necklacePrice

            }
            yield resp

