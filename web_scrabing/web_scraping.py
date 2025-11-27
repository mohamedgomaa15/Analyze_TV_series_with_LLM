import scrapy
from scrapy.crawler import CrawlerProcess

class SpiderClass(scrapy.Spider):
    name = "Naruto_Spider"

    def start_requests(self):
        urls = ['https://naruto.fandom.com/wiki/10_Hit_Combo']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        attack_urls = response.css('.smw-columnlist-container')[0].css("a::attr(href)").extract()
        for attack_url in attack_urls:
            yield response.follow(url=attack_url, callback=self.parse1)

        next_page_url = response.css('a.mw-nextlink::attr(href)').extract()
        if next_page_url:
            for next_page in next_page_url:
                yield response.follow(url=next_page, callback=self.parse)
   
   
    def parse1(self, response):
        jutsu_name = response.css('h1#firstHeading > span.mw-page-title-main::text').extract_first()
        jutsu_description = response.xpath('//div[@id="mw-content-text"]/div[contains(@class, "mw-content-ltr")]/p')[-1].css(' ::text').extract().join().strip()
        jutsu_type = response.xpath('//aside/section')[2].css('a::text').extract_first().strip()
       
        
        
        yield dict (
            jutsu_name = jutsu_name,
            jutsu_type = jutsu_type,
            jutsu_description = jutsu_description
        )
        

 
process = CrawlerProcess(settings={
    "FEEDS": {
        "output.jsonl": {"format": "jsonlines"}
    }
})
process.crawl(SpiderClass)
print("Crawling started...")
process.start()# the script will block here until the crawling is finished
print("Crawling finished.")

# scrapy runspider crwal.py -o output.jsonl