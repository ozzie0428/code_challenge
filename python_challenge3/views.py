from django.shortcuts import render, redirect
from rest_framework import viewsets

from django.http import JsonResponse
 
def phone_numbers_list(request):
    phone_numbers = list()
    file_name = 'code_challenge_data_1.txt'
    with open(file_name) as fo:
        for rec in fo:
            title = rec.strip().replace('(', '')
            title = title.replace(')', '')
            title = title.replace(' ', '')
            title = title.replace('-', '')
            title = title.replace('1-', '')
            title = title.replace('11-', '')
            title = title.replace('11+', '')
            title = title.replace('1+', '')
            title = title.replace('+', '')
            title = title.replace(',', '')
            title = title.replace('#', '')
            title = title.replace('[', '')
            title = title.replace(']', '')
            title = title[0:10]
            title = '({})-{}-{}'.format(title[:3], title[3:6], title[6:])
            phone_numbers.append({"telephone": title})
        return JsonResponse({"results": phone_numbers })


def filter_number(request, areacode):
    phone_numbers = list()
    file_name = 'code_challenge_data_1.txt'
    with open(file_name) as fo:
        for rec in fo:
            title = rec.strip().replace('(', '')
            title = title.replace(')', '')
            title = title.replace(' ', '')
            title = title.replace('-', '')
            title = title.replace('1-', '')
            title = title.replace('11-', '')
            title = title.replace('11+', '')
            title = title.replace('1+', '')
            title = title.replace('+', '')
            title = title.replace(',', '')
            title = title.replace('#', '')
            title = title.replace('[', '')
            title = title.replace(']', '')
            title = title[0:10]
            title = '({})-{}-{}'.format(title[:3], title[3:6], title[6:])
            phone_numbers.append(title)

        foundNumbers = list()
        for rec in phone_numbers:
            if rec.find(str(areacode)) != -1:
                foundNumbers.append(rec)
            else:
                continue
        return JsonResponse({"results": foundNumbers })
