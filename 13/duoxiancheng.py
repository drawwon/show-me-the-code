from bs4 import BeautifulSoup
import uuid
import Queue
import threading
import requests
import time
import os


def get_image_name(href):
    href_list = href.split('/')
    return href_list.pop()


def rename_image(name):
    name_list = name.split('.')
    if name_list is not None and name_list.pop() not in image_suffix():
        name = str(uuid.uuid4()) + '.jpg'
    return name


def image_suffix():
    image_suffixes = ['jpg', 'jpeg', 'png', 'gif']
    return image_suffixes


def create_dir(download_dir):
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)


class LearnSpider:
    def __init__(self, username, password):
        self.queried_set = set()
        self.generate_url_queue = queue.Queue()
        self.download_image_queue = queue.Queue()
        self.session = self.login_zhihu(username, password)

    @staticmethod
    def login_zhihu(username, password):
        data = {
            "email": username,
            "password": password,
            "remember_me": "true",
        }
        login_url = "https://www.zhihu.com/login/email"
        session = requests.session()
        response = session.post(url=login_url, data=data)
        print(response.json())
        return session

    def parse_html(self, path):
        html = self.session.get(path).text
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def generate_path(self, path):
        soup = self.parse_html(path)
        link_list = soup.find_all("a")
        for link in link_list:
            href_value = link.get('href')
            if href_value is not None and href_value.startswith('http'):
                if href_value not in self.queried_set:
                    self.queried_set.add(href_value)
                    self.download_image_queue.put(href_value)

    def download_images(self, path, download_dir):
        self.generate_url_queue.put(path)
        soup = self.parse_html(path)
        a_list = soup.find_all('img')
        for link in a_list:
            src_value = link.get('src')
            if src_value is not None and src_value.startswith('http'):
                print(threading.current_thread().name, " downloading ", src_value)
                name = rename_image(get_image_name(src_value))
                with open("{0}{1}{2}".format(download_dir, os.path.sep, name), 'wb') as outfile:
                    data = self.session.get(src_value).content
                    outfile.write(data)

    def generate_path_work(self):
        while True:
            if not self.generate_url_queue.empty():
                pop_path = self.generate_url_queue.get()
                self.generate_path(pop_path)
            else:
                time.sleep(1)
                print("generate queue is null")

    def download_image_work(self, download_path):
        while True:
            if not self.download_image_queue.empty():
                pop_path = self.download_image_queue.get()
                self.download_images(pop_path, download_path)
            else:
                time.sleep(1)
                print("download queue is null")

    def start_download(self, download_dir, download_thread_count=10):
        create_dir(download_dir)
        path = "https://www.zhihu.com"
        self.download_image_queue.put(path)
        generate_thread = threading.Thread(target=self.generate_path_work, name="generate_path_thread")
        for i in range(1, download_thread_count + 1):
            threading.Thread(target=self.download_image_work, args=(download_dir,), name="thread{0}".format(i)).start()
        generate_thread.start()

if __name__ == "__main__":
    login_username = "***"
    login_password = "***"
    spider = LearnSpider(login_username, login_password)
    spider.start_download("e:\\down_images", download_thread_count=50)