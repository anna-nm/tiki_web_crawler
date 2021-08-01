from bs4 import BeautifulSoup
import urllib.request


url = 'https://tiki.vn/search?q=rau'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')


main = soup.find('div', class_='CategoryViewstyle__Right-sc-bhstkd-1 jxmsjJ')
product = main.find_all('a')
image = main.find_all('img')



def get_name():
    name_list = list()
    for each in product:
        full_name = str(each.find('div', class_='name'))
        name = full_name[24:-13]
        if name == '':
            pass
        else:
            name_list.append(name)
    return name_list
    

def get_price():
    price_list = list()
    for each in product:
        full_price = str(each.find('div', class_='price-discount__price'))
        price = full_price[35:-8]
        if price == 'None':
            pass
        elif price == '':
            pass
        else:
            price_list.append(price)
    return price_list
    

def get_link():
    link_list = list()
    for each in product:
        link = each.get('href')
        if 'https://tiki.vn' in link:
            pass
        else:
            link_list.append('https://tiki.vn{}'.format(link))
    return link_list
    

def get_rate():
    rate_list = list()
    for each in product:
        rating = each.find(class_='average')
        if not rating:
            rate_list.append('Not Available')
        else:
            rate = rating.get('style')
            rate_list.append(rate[6:])
    del rate_list[0:5]
    del rate_list[-7:-1]
    return rate_list
    

def get_image():
    image_list = list()
    for i in image:
        pic = i.get('src')
        if 'ad6d03338.png' in pic:
            pass
        elif '005ad28c.png' in pic:
            pass
        elif '3f8b8e.png' in pic:
            pass
        elif '893662.png' in pic:
            pass
        else:
            image_list.append(pic)
    return image_list
    

def get_sold():
    sold_list = list()
    for each in product:
        sold = str(each.find(class_='styles__StyledQtySold-sc-732h27-2 fCfYNm'))
        if sold == 'None':
            sold_list.append('Not Available')
        else:
            sold_list.append(sold[61:-6])
    del sold_list[0:5]
    del sold_list[-7:-1]
    return sold_list
    

def get_discount():
    discount_list = list()
    for each in product:
        full_price = str(each.find('div', class_='price-discount__discount'))
        price = full_price[47:-15]
        if price == '':
            discount_list.append('0%')
        else:
            discount_list.append(price + '%')
    del discount_list[0:5]
    return discount_list
    


n = get_name()
l = get_link()
i = get_image()
p = get_price()
r = get_rate()
s = get_sold()
d = get_discount()

for c in range(len(n)):
    print('Name: {} \n Price: {} \n Discount: {} \n Rate: {} \n Sold: {} \n Image: {} \n Link: {}\n'.format(n[c], p[c], d[c], r[c], s[c], i[c], l[c]))
