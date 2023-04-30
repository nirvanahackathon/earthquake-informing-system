from django.shortcuts import render

from .models import Tweets

def home_view(request):
    tweets = Tweets.objects.all()
    context = {
        'tweets': tweets,
        'region': 'Tweetlər'
    }
    return render(request, 'index.html', context=context)


def narimanov_view(request):
    tweets = Tweets.objects.filter(region_id=1)
    region = 'Narimanov'
    context = {
        'tweets': tweets,
        'region': region
    }
    return render(request, 'index.html', context=context)

def binagadi_view(request):
    tweets = Tweets.objects.filter(region_id=2)
    context = {
        'tweets': tweets,
        'region': 'Binagadi'
    }
    return render(request, 'index.html', context=context)

def nasimi_view(request):
    tweets = Tweets.objects.filter(region_id=3)
    context = {
        'tweets': tweets,
        'region': 'Nasimi'
    }
    return render(request, 'index.html', context=context)

def khatai_view(request):
    tweets = Tweets.objects.filter(region_id=4)
    context = {
        'tweets': tweets,
        'region': 'Khatai'
    }
    return render(request, 'index.html', context=context)

def yasamal_view(request):
    tweets = Tweets.objects.filter(region_id=5)
    context = {
        'tweets': tweets,
        'region': 'Yasamal'
    }
    return render(request, 'index.html', context=context)

def surakhani_view(request):
    tweets = Tweets.objects.filter(region_id=6)
    context = {
        'tweets': tweets,
        'region': 'Surakhani'
    }
    return render(request, 'index.html', context=context)

def sabayil_view(request):
    tweets = Tweets.objects.filter(region_id=7)
    context = {
        'tweets': tweets,
        'region': 'Sabayil'
    }
    return render(request, 'index.html', context=context)

def nizami_view(request):
    tweets = Tweets.objects.filter(region_id=8)
    context = {
        'tweets': tweets,
        'region': 'Nizami'
    }
    return render(request, 'index.html', context=context)

def namelum_view(request):
    tweets = Tweets.objects.filter(region_id=9)
    context = {
        'tweets': tweets,
        'region': 'Namelum'
    }
    return render(request, 'index.html', context=context)