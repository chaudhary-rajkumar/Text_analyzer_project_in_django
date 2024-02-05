from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercounter=request.POST.get('charactercounter','off')


    if removepunc=='on':
        punctuations='''!()-[]{;}:'"\<>.,/?@#$%^&*_~.'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    

    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    
    elif newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed = analyzed + char
        params={'purpose':'Removed New line','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    
    else:
        return HttpResponse("Error")
    

    # elif fullcaps=='on':
    #     analyzed=""
    #     for char in djtext:
    #         analyzed = analyzed + char.remove
    #     params={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
    #     return render(request,'analyze.html',params)

    # elif newlineremover=='on':
    #     analyzed=""
    #     for char in djtext:
    #         if char!='\n':
    #             analyzed = analyzed + char.()
    #     params={'purpose':'Removed New line','analyzed_text':analyzed}
    #     return render(request,'analyze.html',params)
    
    # elif extraspaceremover=='on':
    #     analyzed=""
    #     analyzed = analyzed + djtext.replace('  ',' ')
    #     params={'purpose':'Removed Extra Space','analyzed_text':analyzed}
    #     return render(request,'analyze.html',params)
    
    # elif charactercounter=='on':
    #     djtext=djtext.lower()
    #     analyzed="" 
    #     for char in range(0,len(djtext)):
    
    #         if djtext[char] not in analyzed:
    #             analyzed = analyzed + djtext[char]
    #             print(f"{djtext[char]} : {djtext.count(djtext[char])}")
    #     params={'purpose':'Total Counted Character is','analyzed_text':analyzed}
    #     return render(request,'analyze.html',params)

    # else:
    #     return HttpResponse("Error")