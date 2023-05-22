from django.shortcuts import render, redirect

from .models import advice_him, advice_jja, advice_sok

import random
# Create your views here.
# 실행안되면 자바스크립트 들여쓰기 문제일 듯
querydict = {}
advice = ''
querydict_category = ''

def start_page(request): # 글 쓰는 페이지 / 종이 꾸겨지는게 다음 페이지로 가는게 아니라면 else 안에 give_advice 함수 넣어야할듯
    global advice
    global querydict
    global querydict_category
    querydict = {}
    advice =''
    querydict_category = ''
    return render(request, 'advices/start_page.html')

def letter(request):
    global advice
    global querydict
    global querydict_category
    querydict = request.GET
    context = {
            'advice':advice
        }
    if querydict == {}:
        print(f'advice: {advice}')
        return render(request, 'advices/letter.html', context)
    else:
        if querydict['category'] == 'him':
            advice = advice_him.objects.get(id=random.randint(1,10)).content
        elif querydict['category'] == 'jja':
            advice = advice_jja.objects.get(id=random.randint(1,11)).content
        elif querydict['category'] == 'sok':
            advice = advice_sok.objects.get(id=random.randint(1,10)).content
        else:
            return render(request, 'advices/letter.html', context)
        print(f'advice:{advice}')
        querydict_category = querydict['category']
        return redirect('letter_page')
    
def trash_can(request):
    context = {
            'category':querydict_category
        }
    print(querydict_category)
    return render(request, 'advices/trashCan.html', context)

def cookie1(request):
    return render(request, 'advices/cookie1.html')

def cookie2(request):
    return render(request, 'advices/cookie2.html')

def last_page(request):
    context={
        'advice':advice
    }
    return render(request, 'advices/LastPage.html', context)

##################### 프론트랑 합치기 전 ########################

# def real_advice(request): # 쿠키 까지고 나오는 플랜카드랑 연결
#     context={
#         'advice':advice
#     }
#     return render(request, 'advices/advice_2.html', context)

# def turn_to_firstpage(request):
#     global advice
#     advice = ''
#     return redirect()
# advice 변수에 전에 썼던 명언이 남아있다고 해도 어차피 다시 할당하니까 초기화 할 필요 없음

# def letter(request):  ## 초기 letter 함수
#     global querydict
#     querydict = request.GET
#     context = {
#         'querydict':querydict
#     }
#     print(querydict)
#     return render(request, 'advices/letter.html')

# def give_advice(request):
#     global advice
#     if querydict['category'] == 'him':
#         advice = advice_him.objects.get(id=random.randint(1,2)).content
#     elif querydict['category'] == 'jja':
#         advice = advice_jja.objects.get(id=random.randint(1,2)).content
#     elif querydict['category'] == 'sok':
#         advice = advice_sok.objects.get(id=random.randint(1,2)).content
#     context = {
#         'advice':advice
#     }
#     return render(request, 'advices/advice.html')