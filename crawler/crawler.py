import requests
import json
from urllib.parse import quote


headers = {
    'Accept': 'application/json',
}
api_url = 'http://api_service:9000/add-list'


def get_list_products(category_url):
    category_url_encode = quote(f"{category_url}&pagetype=1", safe='')
    url = f"https://fptshop.com.vn/apiFPTShop/Product/GetProductList?url={category_url_encode}"
    response = requests.get(url, headers=headers)
    return json.loads(response.text)['datas']['filterModel']['listDefault']['list']


def get_product_details(name_ascii):
    url_detail = f"https://fptshop.com.vn/api-data/API_GiaDung/api/Product/AppliancesAPI/GetProductDetail?name={name_ascii}&url=https:%2F%2Ffptshop.com.vn%2Fdien-thoai"
    response = requests.get(url_detail, headers=headers)

    try:
        product_detail = json.loads(response.text)['datas']['model']['product']
        return {
            'name': product_detail['name'],
            'category': product_detail['productType']['name'],
            'brand': product_detail['brand']['name'],
            'price': int(product_detail['productVariant']['price']),
            'images_url': f"https://fptshop.com.vn/Uploads/Originals/{product_detail['productVariant']['listGallery'][0]['url']}",
        }
    except:
        print(f'Fail to get data {name_ascii}')
        return None


def add_products_to_db(products):
    response = requests.post(api_url, data=json.dumps(products))

    try:
        result = json.loads(response.text)
        result['data_crawl'] = products
        return result
    except:
        return {'type': 'error', 'message': 'Failed to call API to add products', 'data_crawl': products}


def crawl(phone_page, laptop_page, tablet_page):
    list_product_details = []
    list_category_urls = []
    if phone_page:
        list_category_urls.append(
            f'https://fptshop.com.vn/dien-thoai?hang-san-xuat=apple-iphone,samsung,oppo,xiaomi,realme,vivo&trang={phone_page}')
    if laptop_page:
        list_category_urls.append(
            f'https://fptshop.com.vn/may-tinh-xach-tay?hang-san-xuat=apple-macbook,asus,hp,acer,msi,dell&trang={laptop_page}')
    if tablet_page:
        list_category_urls.append(
            f'https://fptshop.com.vn/may-tinh-bang?hang-san-xuat=apple-ipad,samsung,xiaomi,oppo&trang={tablet_page}')

    for category_url in list_category_urls:
        list_products = get_list_products(category_url)

        for product in list_products:
            nameAscii = product['nameAscii']
            product_detail = get_product_details(nameAscii)

            if product_detail:
                list_product_details.append(product_detail)

    return add_products_to_db(list_product_details)
