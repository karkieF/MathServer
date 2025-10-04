
from django.shortcuts import render
def calculate_BMI(request):
    context={}
    context['bmi']="0"
    context['height']="0"
    context['weight']="0"
    if request.method == "POST":
        height = float(request.POST.get("height",'0'))
        weight = float(request.POST.get("weight",'0'))
        print('request=',request)
        print('Height=',height)
        print('Weight=',weight)
        bmi = weight / ((height / 100) ** 2) 
        context['bmi']=bmi
        context['weight']=weight
        context['height']=height
        print('BMI=',bmi)
    return render(request, 'myapp/math.html', context)


