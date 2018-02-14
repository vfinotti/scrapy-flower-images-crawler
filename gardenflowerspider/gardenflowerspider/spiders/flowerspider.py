from gardenflowerspider.items import GardenFlower
import datetime
import scrapy

def extract_whole_text(url):
    url_text = ''
    for item in url:
        url_text = url_text + item.extract()
        
    return url_text

class FlowerSpider(scrapy.Spider):
    name = "garden-flower-spider"
    # URL of plants photos of the last year period
    start_urls = [#"https://garden.org/apps/plant_photos/view/year/popular/0/?q_caption=&q_gallery=",
                  "https://garden.org/apps/plant_photos/view/year/popular/0/?q_caption=&q_gallery=bloom", # just bloom pictures
    ]

    def parse(self, response):
        # picking all 'tr' nodes, no matter where they are, if the subnode
        # 'td/table/tbody/tr/td/b' contains the text 'Plant:'

        url = response.xpath('//tr[./td/table/tbody/tr/td/b[contains(., "Plant:")]]')
        for flowerset in url:
            imageURL = 'https://garden.org' + flowerset.css('img ::attr(src)').extract_first()
            flower_name = extract_whole_text(flowerset.css('a ::text'))

            yield GardenFlower(flower_name=flower_name, file_urls=[imageURL])

    # def parse_page(self, response):
    #     # loop over all cover link elements that link off to the large
    #     # cover of the magazine and yield a request to grab the cover
    #     # data and image
    #     for href in response.xpath("//a[contains(., 'Large Cover')]"):
    #         yield scrapy.Request(href.xpath("@href").extract_first(),
    #     			 self.parse_covers)

    #     # extract the 'Next' link from the pagination, load it, and
    #     # parse it
    #     next = response.css("div.pages").xpath("a[contains(., 'Next')]")
    #     yield scrapy.Request(next.xpath("@href").extract_first(), self.parse_page)


    # def parse_covers(self, response):
    #     # grab the URL of the cover image
    #     img = response.css(".art-cover-photo figure a img").xpath("@src")
    #     imageURL = img.extract_first()

    #     # grab the title and publication date of the current issue
    #     title = response.css(".content-main-aside h1::text").extract_first()
    #     year = response.css(".content-main-aside h1 time a::text").extract_first()
    #     month = response.css(".content-main-aside h1 time::text").extract_first()[:-2]

    #     # parse the date
    #     date = "{} {}".format(month, year).replace(".", "")
    #     d = datetime.datetime.strptime(date, "%b %d %Y")
    #     pub = "{}-{}-{}".format(d.year, str(d.month).zfill(2), str(d.day).zfill(2))

    #     # yield the result
    #     yield MagazineCover(title=title, pubDate=pub, file_urls=[imageURL])
        
