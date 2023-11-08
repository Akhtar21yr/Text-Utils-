from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fulcaps = request.POST.get('fulcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')

    if removepunc == 'on':
        analyzed = ''
        punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
'''
        for char in djtext:
            if char not in punctuation :
                analyzed += char
        djtext = analyzed

    if fulcaps == 'on':
        analyzed = djtext.upper()
        djtext = analyzed

    if newlineremover =='on' :
        analyzed = ''
        for char in djtext:
            if not (char != '\n' and char != '\r'):
                analyzed += " "
            if char != '\n' and char != '\r':
                analyzed += char
        djtext = analyzed

    if extraspaceremove =='on':
        analyzed = ' '
        for char in djtext:
            if not (analyzed[-1] == ' ' and char == ' ') :
                analyzed += char
        djtext = analyzed[1:]
        
    params = {'analyzed_text':djtext}
    return render(request,'analyze.html',params)
    


