# Ex.05 Design a Website for Server Side Processing
## Date:04/10/25

## AIM:
 To design a website to calculate the  Body Mass Index(BMI)server side. 


## FORMULA:
BMI= W/H<sup>2</sup>
<br> BMI -->Body Mass Index
<br> W -->Weight
<br> H -->Height

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<html>
    <head>
        <title>BMI Calculator</title>
        <style type="text/css">
            body{
                border: solid rgb(41, 90, 237) 10px;
                background-color: rgb(11, 57, 103);
            }
            .value{
                text-align: center;
                padding: 40px;
                width: 400px;
                height: 30px;
                font-size: 30px;
                background-color: rgb(64, 112, 201);
                margin:auto;

            }
            h1,h2,h3{
                text-align: center;
                font-size: xx-large;
                padding: 20px;
            
            }
            button{
                padding: 15px;
                width: 250px;
                border-radius: 25px;
                border:solid black 5px;
                background-color: rgb(22, 68, 74);
                font-size: 20px;
            } 
            h3{
                padding: 20px 50px;
                text-align: center;
                border: 10px solid rgb(23, 46, 55);
                background-color: rgb(141, 144, 247);
                width: 380px;
                margin: 20px auto;

            }
            input{
                padding: 10px;
            }
        </style>
    </head>
    <body>
    <h1>karkie F(25016839)</h1>
    <h2>Body Mass Index (BMI) Calculator</h2>
    <form method="post">
        {% csrf_token %}
        <div class="value">
        <label>Height (cm):</label>
        <input type="text" name="height" required>
        </div>
        <div class="value">
        <label>Weight (kg):</label>
        <input type="text" name="weight" required>
        </div>
        <div class="value">
        <button type="submit" >Calculate BMI</button>
        </div>
    <h3>Your BMI: {{bmi}}</h3>
    </form>
    </body>
</html>


views.py

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


urls.py

from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns =[
    path('admin/', admin.site.urls),
    path('Body Mass Index/',views.calculate_BMI,name="Body Mass Index"),
    path('',views.calculate_BMI,name="Body Mass Index")
]
```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot (34).png>)

## HOMEPAGE:
![alt text](<Screenshot (36).png>)

## RESULT:
The program for performing server side processing is completed successfully.
