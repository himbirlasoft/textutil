from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    
    return render(request,'index2.html')
    #return HttpResponse("Hello Himanshu")


def analyzer(request):
    djtext=request.POST.get('text','defaut')
    removepunc=request.POST.get('removepunc','off')
    capital=request.POST.get('capital','off')
    newline=request.POST.get('newline','off')
    if removepunc=="on":
        print(djtext)
        print(removepunc)
        analyse=""
        Punctuation='''<,.:;"'?/}]|{[}]=+-_)(*&^%$#@!~`'''
        for char in djtext:
            if char not in Punctuation:
                analyse=analyse+char
        params={'purpose':'Removed Punctuation','analysed_text':analyse}
        return render(request,'analyser.html',params)
    elif(capital=='on'):
        print(djtext)
        print(removepunc)
        analyse=""
        Punctuation='''<,.:;"'?/}]|{[}]=+-_)(*&^%$#@!~`'''
        for char in djtext:
            if char not in "":
                analyse=analyse+char.upper()
        params={'purpose':'Capitalised Text','analysed_text':analyse}
        return render(request,'analyser.html',params)
    elif(newline=='on'):
        print(djtext)
        print(removepunc)
        analyse=""
        Punctuation='''<,.:;"'?/}]|{[}]=+-_)(*&^%$#@!~`'''
        for char in djtext:
            if(char!='\n'):
                analyse=analyse+char
        params={'purpose':'Without Newline','analysed_text':analyse}
        return render(request,'analyser.html',params)
    else:
        return HttpResponse("I dont Give a Fuck")
    

