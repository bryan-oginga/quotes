import requests
from django.shortcuts import render
from .models import Quotes  


def random_quotes(request):
    
    quote_api_url = 'https://zenquotes.io/api/random'
    picsum_image_url = 'https://picsum.photos/800/600'  
    

    # Fetching a random quote
    quote_response = requests.get(quote_api_url)
    quote = "No quote available."
    author = "Unknown"
    
    # Check if quote API response is valid
    if quote_response.status_code == 200:
        quote_data = quote_response.json()
        if isinstance(quote_data, list) and len(quote_data) > 0:
            quote = quote_data[0]['q']
            author = quote_data[0]['a']

    # Generate a random image URL
    image_url = picsum_image_url

    # Save quote, author, and image to the database
    Quotes.objects.create(quote_text=quote, author_name=author, image_url=image_url)

    context = {
        'quote': quote,
        'author': author,
        'image_url': image_url,
    }

    return render(request, 'random_quotes.html', context)
