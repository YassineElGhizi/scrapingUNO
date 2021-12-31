import requests
from bs4 import BeautifulSoup as BS
from time import sleep

html = """
<div class="product-hover">
    <h2 class="product-name"><a href="https://uno.ma/apple-iphone-13-pro-max-128-gb-bleu-alpin-neuf-1-an-de-garantie-maroc" title="Apple iPhone 13 Pro Max 128 Gb Bleu Alpin (Neuf, 1 An de Garantie)">Apple iPhone 13 Pro Max 128 Gb Bleu Alpin (Neuf, 1 An de Garantie)</a></h2><br/>
    <div class="price-box">
        <p class="special-price">
            <span class="price-label">Prix UNO.ma :</span>
            <span class="price" style=" text-decoration: none; " id="product-price-3022">
            15 490,00 MAD </span>
        </p>
        <p class="old-price">
            <span class="price-label">Prix ailleurs:</span>
            <span class="price" style=" text-decoration: none; " id="old-price-3022">
            15 690,00 MAD </span>
        </p>
    </div>
</div>
"""

cards_links = list()
items = BS(
    html ,
    features="html.parser"
)

target_item = items.findAll('h2' , {'class' ,'product-name' }  )
price = ((items.findAll('span' , {'class' , 'price'})[1]).text).strip()

target_item.append('<strong>{}</strong>'.format(price))


stockage_list = ['128 Gb','256 Gb','512 Gb','1 Tb' ]
def check_stockage(mystr):
    for i in stockage_list:
        if i in mystr:
            return i
        return 0



for i in target_item:
    tmp = BS




