# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
import requests as rq
from flipkart.utils.dbConfig import laptopdb

def getImageName(imgName):
    base_name = imgName.rsplit('.', 1)[0]
    new_name = re.sub(r'[^A-Za-z0-9]+', '_', base_name)
    save_path = f'{new_name}.png'
    return save_path

def downloadImg(imgUrl, imageName):
    try:
        response = rq.get(imgUrl)
        response.raise_for_status()  # Raise HTTPError for bad responses
        with open(imageName, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {imageName}")
    except rq.exceptions.RequestException as e:
        print(f"Failed to download image. Error: {e}")


class FlipkartPipeline:
    def process_item(self, item, spider):

        image_name = getImageName(item['img_name'])
        downloadImg(item['image_url'], image_name)
        laptopdb(item)

        return item