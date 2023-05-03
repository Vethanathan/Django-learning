from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,"base.html")

def check(request):
    String = request.GET["String"]
    result = "Palindrome" if String == String[::-1] else "Not a Palindrome"
    return render(request,"base.html",{'result':result})