from django.contrib import admin
from .models import Amazon_Data, Flipkart_Data, Scrap_links
# Register your models here.
admin.site.register(Amazon_Data)
admin.site.register(Flipkart_Data)
admin.site.register(Scrap_links)
