from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os
import shutil

import logger


class CfPageHandler():
    def __init__(self):
        self._temp_folder_path = ''
        self.logger = logger.create_logger()
#        self.inp_w = [
#            {'url':"https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0", 'dest': 'w0.html'},
#            {'url':"https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=2", 'dest': 'w1.html'}
#        ]


    def create_tmp_dir(self):
        dir_path = os.path.dirname(__file__)
        self._temp_folder_path = os.path.join(dir_path, 'temp_folder')

        if os.path.exists(self._temp_folder_path):
            shutil.rmtree(self._temp_folder_path)
        os.mkdir(self._temp_folder_path, mode = 0o777)
        self.logger.debug("tmp dir created: {}".format(self._temp_folder_path))
    
    def get_tmp_dir(self):
        return self._temp_folder_path

    def remove_tmp_dir(self):
        if os.path.exists(self._temp_folder_path):
            shutil.rmtree(self._temp_folder_path)
        self.logger.debug("tmp dir deleted: {}".format(self._temp_folder_path))


    def save_htmls(self, inps):

        for inp in inps:
            #driver = webdriver.Chrome(service=ChromeService( 
            #    ChromeDriverManager().install())) 
            driver = webdriver.Firefox()

            driver.implicitly_wait(30)
            driver.get(inp['url'])
            driver.implicitly_wait(30)

            time.sleep(5)

            html = driver.page_source

            dest_file = os.path.join(self._temp_folder_path, inp['dest'])
            with open(dest_file, 'w') as file:
                file.write(html)
            self.logger.debug("html ({}) saved to {}".format(inp['url'], dest_file))
            driver.quit()

    def collect(self, inp_dict):
        self.create_tmp_dir()
        self.save_htmls(inp_dict)
        return self.get_tmp_dir()
        #self.remove_tmp_dir()

#a = CfPageHandler()
#a.collect()