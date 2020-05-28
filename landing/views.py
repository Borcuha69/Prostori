from django.shortcuts import render


def main(requests):
    return render(requests, 'landing/main.html', locals())