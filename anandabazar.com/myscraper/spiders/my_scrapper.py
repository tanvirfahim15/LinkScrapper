import scrapy
from scrapy.linkextractor import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from myscraper.items import MyscraperItem

def urlShortener(url):
    return url

class MyScrapperSpider(CrawlSpider):
    name = 'my-scrapper'
    
    # The domains that are allowed (links to other domains are skipped)
    allowed_domains = ["anandabazar.com"]

    # The URLs to start with
    start_urls = ["https://www.anandabazar.com/"]
    
    
    # This spider has one rule: extract all (unique and canonicalized) links, follow them and parse them using the parse_items method
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    # Method for parsing items
    def parse_items(self, response):
        # The list of items that are found on the particular page
        items = []
        # Only extract canonicalized and unique links (with respect to the current page)
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        # Now go through all the found links
        for link in links:
            # Check whether the domain of the URL of the link is allowed; so whether it is in one of the allowed domains
            is_allowed = False
            for allowed_domain in self.allowed_domains:
                if allowed_domain in link.url:
                    is_allowed = True
            # If it is allowed, create a new item and add it to the list of found items
            if is_allowed:
                item = MyscraperItem()
                item['link'] = link.url
                items.append(item)
                patterns = ["anandabazar.com/sport","anandabazar.com/business","anandabazar.com/entertainment","anandabazar.com/bangladesh-news","anandabazar.com/international"]

                file = None
                if patterns[0] in link.url:
                    file= open('../../data/sports.csv','a')
                if patterns[1] in link.url:
                    file= open('../../data/economy.csv','a')
                if patterns[2] in link.url:
                    file= open('../../data/entertainment.csv','a')
                if patterns[3] in link.url:
                    file= open('../../data/bangladesh.csv','a')
                if patterns[4] in link.url:
                    file= open('../../data/international.csv','a')

                if file != None:
                    file.write(urlShortener(link.url)+"\n")
                    file.close()


        # Return all the found items
        return items
