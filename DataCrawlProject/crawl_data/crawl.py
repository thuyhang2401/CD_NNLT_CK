import os
import requests
from bs4 import BeautifulSoup
from threading import Thread
from apscheduler.schedulers.background import BackgroundScheduler
import json

class GlassesCrawlerThread(Thread):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/90.0.4430.212 Safari/537.36'
    }

    def __init__(self, pages, category, page_for_thread):
        Thread.__init__(self)
        self.pages = pages
        self.url = 'https://www.glasses.com/AjaxLoadMoreCategoryDisplay?searchPage=&searchTerm=&beginIndex={' \
                   '}&categoryId=' + str(
            category) + '&pageSize=13&catalogId=23201&langId=-1&storeId=15951&crawler=&'
        self.results = []
        self.page_for_thread = page_for_thread
    # When start thread this function is called
    # Crawl all page in a category

    def run(self):
        for i in range(self.pages - self.page_for_thread, self.pages):
            self.crawling(i)

    def parse(self, html):
        links = html.find_all('a', class_='item_container_pdplink')
        for li in links:
            glasses_name = li.find('div', class_='style-name').text
            brand_name = li.find('div', class_='brand-name').text
            price = li.find_all('span', {'class': 'highlight'})[-1].text
            price = price.replace('$ ', '')
            img_url = li.find('img', class_='item-thumbnail')['data-original']
            self.results.append({
                'glasses_id': str(li.get('href').split('/')[-1]),
                'link': 'https://www.glasses.com' + li.get('href'),
                'glasses_name': glasses_name,
                'brand_name': brand_name,
                'price': price,
                'img_url': img_url
            })

    # crawling by index page each page apart 13 degree
    def crawling(self, beginIndex):
        index = beginIndex * 13
        rs = requests.get(self.url.format(index), headers=self.header)
        html = BeautifulSoup(rs.content, 'html.parser')
        self.parse(html)


class DataCrawling:

    def __init__(self):
        with open('crawl_data/config.json') as f:
            config = json.load(f)
        crawl_cfg = config['crawling']
        self.crawler_delay = crawl_cfg['delay']
        self.category_number = crawl_cfg['number_of_category']
        self.scheduler = BackgroundScheduler()
        self.data = {
            'glasses_list': []
        }

    def crawling(self):
        s_category = 99958778
        e_category = 99958819
        threads = []
        page_for_thread = 5
        url = 'https://www.glasses.com/AjaxLoadMoreCategoryDisplay?searchPage=&searchTerm=&beginIndex=0&categoryId={' \
              '}&pageSize=13&catalogId=23201&langId=-1&storeId=15951&crawler=&'

        if s_category + self.category_number > e_category:
            print('_______Number category out of index_______')
        else:
            for i in range(self.category_number):
                response = requests.get(url.format(s_category + i), headers=GlassesCrawlerThread.header)
                soup = BeautifulSoup(response.content, 'html.parser')
                try:
                    total_page = int(soup.find('span', class_='paging').text.split()[3])
                    print(str(total_page) + ' pages of ' + str(s_category + i))
                except Exception as e:
                    print(e)
                    continue

                num_thread = total_page // page_for_thread
                odd = total_page % page_for_thread
                for j in range(1, num_thread + 1):
                    thr = GlassesCrawlerThread(pages=page_for_thread * j, category=(i + s_category),
                                               page_for_thread=page_for_thread)
                    threads.append(thr)
                    thr.start()

                if odd > 0:
                    thread = GlassesCrawlerThread(pages=total_page, category=i + s_category, page_for_thread=odd)
                    threads.append(thread)
                    thread.start()

            [thr.join() for thr in threads]
            self.data = [result for thr in threads for result in thr.results]
            self.save_to_json()
    def timer_crawl(self):
        self.scheduler.add_job(self.crawling, 'cron',
                               hour=self.crawler_delay["hour"],
                               minute=self.crawler_delay["minute"])
        self.scheduler.start()

    def save_to_json(self):
        data_path = os.getenv("DATA_FILE_PATH", "data_crawl/data.json")
        os.makedirs(os.path.dirname(data_path), exist_ok=True)
        with open(data_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def reset_data(self):
        self.data.clear()