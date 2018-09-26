import scrapy


class BlogSpider(scrapy.Spider):
    name = "blogs"
    start_urls = [
        'https://techcrunch.com'
    ]

    def parse(self, response):
        for topic in response.css('div.post-block'):
            yield {
                'article-title': topic.css('a::text').extract_first()[5:-3],
                'article-link': topic.css('a::attr(href)').extract_first(),
                'article-image' : topic.css('img::attr(src)').extract_first(), 
                'article-author': topic.css('a::text').extract()[1][5:-3],
                'author-link': topic.css('a::attr(href)').extract()[1],
            }
        '''
        #to process individual articles
        for topic in response.css('div.post-block'):
            yield response.follow(topic.css('a::attr(href)').extract_first(), callback=self.article_parse)

    def article_parse(self, response):
        #this will parse the articles using the 'article-link'
        '''