from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.urls import reverse
from demoapp.forms import LogForm



# Create your views here.
def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "home.html", context)

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
