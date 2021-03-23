# WebScraping 

Webscraping an e-commerce website using scrapy to fetch necklace Sets information

1. Create a virtual environment:
      
                 python3 -m virtualenv env
      
2. Activate the virtual environment:

                  cd venv/Scripts/activate
     
3. Install requirements:
      
                  pip install scrapy or python3 -m pip install -r requirements.txt
     
4. Go to the project directory and run:

                  cd scraper

                  scrapy crawl necklaceSets
      
5. For JSON extracted data run:

                  scrapy crawl necklaceSets -o necklaceSets.json

6.  For CSV extracted data run:

                  scrapy crawl necklaceSets -o necklaceSets.csv
      
7. Find JSON and CSV file in project directory (scraper).


