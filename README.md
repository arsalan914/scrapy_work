Using docker to run scrapy:
cd into the extracted folder and run the commands

>docker build -t scrapy .

>docker  run -dt --name blog-scrap -p 80:80 scrapy

>docker exec blog-scrap scrapy runspider app/blog_scrap/blog_scrap/spiders/blog_spider.py -o file.json

>docker ps -aqf  "name= blog-scrap" (note the id returned by this command)

>docker cp <id>:file.json .

Run scapy on ur machine directly if you have scrapy installed:
>srapy runspider blog_scrap/blog_scrap/spiders/blog_spider.py -o file,json
