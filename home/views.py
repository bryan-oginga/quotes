import requests
from django.shortcuts import render
from .models import Quotes

def random_quotes(request):
    
    #1. api endpoints
    quote_api_url = 'https://zenquotes.io/api/ramdom/'
    picsum_api_url = 'https://picsum.photos/800/600'
    
    quote_resposne = requests.get(quote_api_url)
    image_response = requests.get(picsum_api_url)
    
    #set defautl values
    quote = "No quote available",
    author = "No author available",
    image_url = None
    
    if quote_resposne.status_code == 200 and image_response.status_code == 200:
        quote_data = quote_resposne.json()
        image_url = image_response.url
        
        if isinstance(quote_data,list) and len(quote_data) > 0:
            quote = quote_data[0].get('q','No quote available')
            author = quote_data[0].get('a','No author available')
            
    Quotes.objects.create(quote_text=quote, author_name=author, image_url=image_url)
        
    context = {
        'quote': quote,
        'author': author,
        'image_url': image_url,
        
        
    }
    return render(request, 'random_quotes.html',context)

