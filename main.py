import time

import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

s = Service('/Users/ramiyammine/Developement/chromedriver')
albumaty_downloadable_driver = webdriver.Chrome(service=s)
albumaty_driver = webdriver.Chrome(service=s)


#
# tracks = anghami_driver.find_elements(By.CLASS_NAME,'cell-title')
#
# all_tracks = []
#
# for i in tracks:
#     all_tracks.append(i)
#
#
albumaty_driver.get('https://www.albumaty.com/')

each_track = albumaty_driver.find_elements(By.CSS_SELECTOR, '.pull-right div .pull-right a')
final_tracks = []

for i in each_track:
    link = i.get_attribute('href')
    if not 'singer' in str(link) :
        if not 'album/' in str(link):
            final_tracks.append(link)

albumaty_driver.close()
time.sleep(5)

for i in final_tracks:
    albumaty_downloadable_driver.get(i)
    download_button = albumaty_downloadable_driver.find_element(By.CLASS_NAME,'singerblockxxx')
    download_button.click()
    time.sleep(10)
    final_download_button = albumaty_downloadable_driver.find_element(By.XPATH,'/html/body/div[4]/div/div/a')
    final_download_button.click()
    time.sleep(20)





