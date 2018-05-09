from sugarcanespyder.items import SugarcaneItem
import datetime
import scrapy
import time

def extract_whole_text(url):
    url_text = ''
    for item in url:
        url_text = url_text + item.extract()
        
    return url_text

class SugarcaneSpider(scrapy.Spider):
    name = "sugarcane-spider"
    # URL of plants photos of the last year period
    start_urls = ['https://www.shutterstock.com/search?search_source=base_landing_page&language=en&searchterm=+plantation+sugarcane&image_type=all',
   ] 

    def parse(self, response):

        # Finds the current page. 'page_info' is in the following format: "Page
        # XX of YY • ". Splitting it at the spaces, the current page (XX) is
        # the element [1] and the last page (YY) is the element [3]
        # search the text of any node whose class is 'page-max', and then extraxct the first result
        # page_info = response.xpath("//*[contains(@class, 'page-max')]/text()").extract_first()
        last_page = int(response.xpath("//*[contains(@class, 'page-max')]/text()").extract_first())
        current_page = int(response.xpath("//*[contains(@class, 'pagination-container id')]//*[contains(@class, 'form-control')]/@value").extract_first())
        print(current_page)

        # picking all nodes if the class is 'img-wrap', no matter where they
        # are, and then selecting the 'src' attriute (it's where the image URL
        # is) from 'img' nodes
        images = response.xpath("//*[contains(@class, 'img-wrap')]//img/@src")
        imagesURLs = images.extract()

        for imageURL in imagesURLs:
            yield SugarcaneItem(page=current_page, file_urls=[imageURL])
        
        # # reload page if there are less then 20 pictures and it is not the last
        # # page
        # if ((len(url) < 20) and (current_page != last_page)) :
        #     next_page = 'https://garden.org/apps/plant_photos/view/year/popular/0/?q_caption=&q_gallery=bloom&offset=' + str(20*(current_page-1))
        #     yield scrapy.Request(
        #         response.urljoin(next_page),
        #         dont_filter = True,
        #         callback=self.parse
        #     )

        # Test if current page is the last. If not, go to next page
        if (current_page < last_page):
            next_page = 'https://www.shutterstock.com/search?searchterm=%20plantation%20sugarcane&sort=popular&image_type=all&search_source=base_landing_page&language=en&page=' + str(current_page + 1)
            yield scrapy.Request(
                response.urljoin(next_page),
                dont_filter = True,
                callback=self.parse
            )
