from django.shortcuts import render
from .models import Cofee
# Create your views here.
def index(request):
    list_cofee=Cofee.objects.all()
    # list_cofee=[Cofee1,Cofee2,Cofee3,Cofee4,Cofee5]
    Splitted_Cofee=[]
    for i in range(0,len(list_cofee),4):
        Splitted_Cofee+=[list_cofee[i:i+4]]
    print(Splitted_Cofee)
    return render(request,"index.html",{"Splitted_Cofee":Splitted_Cofee})