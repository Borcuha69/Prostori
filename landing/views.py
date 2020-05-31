from django.shortcuts import render


def main(requests):
    return render(requests, 'landing/main.html', locals())

def about(requests):
    return  render(requests, 'landing/about.html', locals())

def contacts(requests):
    return  render(requests, 'landing/contacts.html', locals())