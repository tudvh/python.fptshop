import requests
import json
from urllib.parse import quote


headers = {
    'Accept': 'application/json',
}


def crawl(phone_page, laptop_page, tablet_page):
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

    list_product_details = []

    for category_url in list_category_urls:
        category_url_encode = quote(f"{category_url}&pagetype=1", safe='')
        url = f"https://fptshop.com.vn/apiFPTShop/Product/GetProductList?url={category_url_encode}"

        response = requests.request(
            "GET", url, headers=headers)

        list_products = json.loads(response.text)[
            'datas']['filterModel']['listDefault']['list']

        for product in list_products:
            nameAscii = product['nameAscii']
            url_detail = f"https://fptshop.com.vn/api-data/API_GiaDung/api/Product/AppliancesAPI/GetProductDetail?name={nameAscii}&url=https:%2F%2Ffptshop.com.vn%2Fdien-thoai"
            response = requests.request(
                "GET", url_detail, headers=headers)
            product_detail = json.loads(response.text)[
                'datas']['model']['product']

            list_product_details.append({
                'category': product_detail['productType']['name'],
                'name': product_detail['name'],
                'slug': product_detail['nameAscii'],
                'price': int(product_detail['productVariant']['price']),
                'images_url': f"https://fptshop.com.vn/Uploads/Originals/{product_detail['productVariant']['listGallery'][0]['url']}",
            })

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(list_product_details, f, ensure_ascii=False, indent=4)

    return list_product_details
