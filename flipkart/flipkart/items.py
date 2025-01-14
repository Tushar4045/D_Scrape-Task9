# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags
import re


def convertPrice(price):
    try:
        cleaned_amount = re.sub(r'[^\d.]', '', price)
        amount_float = float(cleaned_amount)
        return amount_float;
    except:
        return 0




class FlipkartItem(scrapy.Item):
    img_name = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),

    )

    image_url = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),

    )
    title = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, convertPrice),
        output_processor=TakeFirst(),
    )

