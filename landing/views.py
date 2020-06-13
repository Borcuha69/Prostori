from django.shortcuts import render


def main(requests):
    return render(requests, 'landing/main.html', locals())

def about(requests):
    return  render(requests, 'landing/about.html', locals())

def contacts(requests):
    return  render(requests, 'landing/contacts.html', locals())

def baths(requests):
    return  render(requests, 'landing/baths.html', locals())

def fermer(requests):
    return render(requests, 'landing/fermer.html', locals())

def activity(requests):
    return  render(requests, 'landing/activity.html', locals())

def fishing(requests):
    return  render(requests, 'landing/fishing.html', locals())

def horsewalking(requests):
    return  render(requests, 'landing/horsewalking.html', locals())

def zoo(requests):
    return  render(requests, 'landing/zoo.html', locals())