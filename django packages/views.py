from django.http import HttpResponse, response
from django.shortcuts import render
def home(request):
    return render(request,"index.html")
def analyze(request):
    text = request.GET.get("textarea")
    checkvalue = request.GET.get("capitalize","off")
    checkvalue2 = request.GET.get("removepunc","off")
    checkvalue3 = request.GET.get("toupper","off")
    checkvalue4 = request.GET.get("charcount","off")
    if checkvalue=="on":
        output={
            "result":""
        }
        captext = text.capitalize()
        output={
            "result":captext
        }
        return render(request,"index.html",output)
    elif checkvalue2=="on":
          output={
        "result":""
          }
          punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
          at=""
          for char in text:
            if char not in punc:
                at = at+char
                output={
                "result":at
                 }
          return render(request,"index.html",output)
    elif checkvalue3=="on":
          output={
        "result":""
          }
          uppertext=text.upper()
          output={
            "result":uppertext
         }
          return render(request,"index.html",output)

    elif checkvalue4=="on":
         output={
        "result":""
          }
         charcount=len(text)
         output={
        "result":f"{charcount} character in given string including Space"
          }
         return render(request,"index.html",output)


    else:
       
        output={
            "result": "Error ! please specify any Operation"}
        return render(request,"index.html",output)

         
    