import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

from .models import Flipkart_Data, Amazon_Data, Scrap_links


def Home(request):
    if request.method == "POST":
        text = request.POST['search-text']
        amazon = Amazon_Data.objects.filter(product_type__icontains=text)
        flipkart = Flipkart_Data.objects.filter(product_type__icontains=text)
        search = True
        search_data = zip(flipkart, amazon)
    return render(request, "index.html", locals())


def flipkart_scrapper(request):
    if request.method == "POST":
        url = request.POST['url']
        product = request.POST['product-type']
        r = requests.get(url)
        html_content = r.content
        complete_data = html_content
        Scrap_links.objects.create(
            link=url,
            product_type=product,
            website="flipkart"
        )

        
        soup = BeautifulSoup(complete_data, "html.parser")
        container = soup.find_all("div", class_="_2kHMtA")
        count = 0
        for i in container:
            count = count + 1
            titles = i.find_all("div", class_="_4rR01T")
            details = i.find_all("li", class_="rgWa7D")

            images = i.find('img', class_="_396cs4")
            current_price = i.find_all('div', class_="_30jeq3 _1_WHN1")
            # mrp = i.find('div', class_="_3I9_wc _27UcVY")
            img_url = images['src']
            title = titles[0].text
            price = current_price[0].text
            discount_price = price.replace("₹", '').replace(",", "")

            Flipkart_Data.objects.create(
                title=title,
                product_type=product,
                price=int(discount_price),
                details=details,
                image=img_url
            )

        data = Flipkart_Data.objects.all().order_by("-id")[:count]
        print(data)
    return render(request, "flipkart_scraper.html", locals())


def amazon_scrapper(request):
    if request.method == "POST":
        headers = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
            "action": "sign-in",
            "email": "6280869135",
            "password": "Mohan@123"
        }

        url = request.POST['url']
        product = request.POST['product-type']
        r = requests.get(url, headers=headers)

        html_content = r.content

        Scrap_links.objects.create(
            link=url,
            product_type=product,
            website="amazon"
        )

        complete_data = html_content
        soup = BeautifulSoup(complete_data, "html.parser")
        details = soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")
        discount_price = soup.find_all("span", class_="a-price-whole")

        images = soup.find_all("img", class_="s-image")

        for i, j, k in zip(details, discount_price, images):
            print(j.get_text())

            Amazon_Data.objects.create(
                title=i.get_text(),
                product_type=product,
                price=j.get_text(),
                image=k['src']
            )
        data = Amazon_Data.objects.all().order_by("-id")

    return render(request, "amazon_scraper.html", locals())
