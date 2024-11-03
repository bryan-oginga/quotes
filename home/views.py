import requests
from django.shortcuts import render
from .models import Quotes

def random_quotes(request):
    
    # 1. api endpoint for random quotes
    quote_api_url = 'https://zenquotes.io/api/random'
    picsum_api_url = 'https://picsum.photos/800/600'
    
    quote_response = requests.get(quote_api_url)
    picsum_response = requests.get(picsum_api_url)
    
    #2. set default values for quote and image
    quote = "No quote available"
    author = "Unknown"
    image_url = None 
    
    #3. check if responses are successful
    if quote_response.status_code == 200 and picsum_response.status_code == 200:
        quote_data = quote_response.json()
        image_url = picsum_response.url
        if isinstance(quote_data,list) and len(quote_data) > 0:
            quote = quote_data[0].get('q', "No quote available")
            author = quote_data[0].get('a', "Unknown")
            
    Quotes.objects.create(quote_text=quote, author_name=author, image_url=image_url)
    
    context = {
        'quote': quote,
        'author': author,
        'image_url': image_url,
        
    }
    return render(request,'random_quotes.html',context)

