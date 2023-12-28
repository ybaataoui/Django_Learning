from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse
from demoapp.forms import LogForm
from .models import Menu



# Create your views here.
def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)

def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
    return render(request, "about.html", {'content':about_content})

# def menu(request):
#     newMenu = {'mains':[
#         {'name':'Classic Pizza', 'price': 10},
#         {'name':'Vegetarian Pizza', 'price':8},
#         {'name':'Gyro', 'price':12},
#     ]}
#     return render(request, "menu.html", newMenu)

def menu_by_id(request):
    newMenu = Menu.objects.all()
    newMenu_dict = {'menu': newMenu}
    return render(request, 'menu_card.html', newMenu_dict)

# def index(request):
#     return HttpResponsePermanentRedirect(reverse('demoapp:login'))

# def home(request):
#     path = request.path
#     scheme = request.scheme
#     method = request.method
#     address = request.META['REMOTE_ADDR']
#     user_agent = request.META['HTTP_USER_AGENT']
#     path_info = request.path_info

#     response = HttpResponse()
#     response.headers['Age'] = 20

#     msg = f"""<br>
#         <br>Path: {path}
#         <br>Address: {address}
#         <br>Scheme: {scheme}
#         <br>Method: {method}
#         <br>User agent: {user_agent}
#         <br>Path info: {path_info}
#         <br> Response header: {response.headers}
#         <br>

#     """ 
#     return HttpResponse(msg, content_type = 'text/html', charset='utf-8')

# def qryview(request):
#     name = request.GET['name']
#     id = request.GET('id')
#     return HttpResponse("Name:{} USerID:{}".format(name, id))

# def showform(request):
#     return render(request, "form.html")

# def getform(request):
#     if request.method == "POST":
#         id = request.POST['id']
#         name = request.POST['name']
#     return HttpResponse("Name:{} UserID:{}".format(name, id))

# def menuitems(request, dish):
#     items = {
#         'pasta': 'Pasta is a type of',
#         'falafel': ' Falafil are deep fried patties',
#         'cheescake': 'Cheesecake is a type of dessert'
#     }

#     description = items[dish]

#     return HttpResponse(f"<h2> {dish} </h2>" + description)

# def loginform(request):
#     return render(request, "login.html")
