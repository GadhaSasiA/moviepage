from django.shortcuts import render,HttpResponse
from.models import Details
from django.contrib import messages
from.forms import LoginForm,UserRegistration,SearchForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

#from django.http import 
from django.shortcuts import redirect


# Create your views here.

def index(request):
    return render(request,'index.html')

def movie_times(request):
    return render(request,'movie_times.html')

def home(request):
    return render(request,'home.html')

def favourites(request):
    return render(request,'favourites.html')

def add_to_favourite(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        favourite_movies = request.session.get('favourite_movies', [])
        if movie_id not in favourite_movies:
            favourite_movies.append(movie_id)
            request.session['favourite_movies'] = favourite_movies
            messages.success(request, 'Added to Favourites successfully.')
        else:
            messages.warning(request, 'This movie is already in your Favourites.')
        return redirect('about')  
    return redirect('about') 


def favourite_movies(request):
    favourite_movie_ids = request.session.get('favourite_movies', [])
    favourite_movies =Details.objects.filter(id__in=favourite_movie_ids)
    return render(request, 'favourites.html', {'favourite_movies': favourite_movies})




def about(request):
    dict_det = {
        'about': Details.objects.all()
    }
    return render(request,'about.html', dict_det)

#def login(request):
    #dict_det = {
        #'about': Details.objects.all()
    #}
    #return render(request,'login.html',) #dict_det)

#@login_required
def user_login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
               login(request,user)
               return render(request,'login.html',{'form':form})
            else:
                return HttpResponse("Invalid login")
        else:
            return render(request, 'user_login.html', {'form': form, 'error_message': 'Invalid form data'})
    
    else:
        form=LoginForm()
        return render(request,'user_login.html',{'form':form})

def user_register(request):
    if request.method=="POST":
        form=UserRegistration(request.POST)

        if form.is_valid():
           new_user=form.save(commit=False)
           new_user.set_password(form.cleaned_data['password'])
           new_user.save()
        return HttpResponse("you are successfully Register")

    else:
        form =UserRegistration()
        return render(request, 'user_register.html', {'form': form})
    

def insertData(request):
    data = Details.objects.all()
    dict = {"data" : data}
    if request.method == "POST":
        img= request.POST.get('img')
        movie_name = request.POST.get('movie_name')
        language = request.POST.get('language')
        genre = request.POST.get('genre')
        duration = request.POST.get('duration')


        print(img,movie_name,language,genre,duration)

        fm =Details(img=img,movie_name=movie_name,language =language,genre = genre,duration = duration)
        fm.save()

    return render(request,'Add.html',dict)

def updateData(request,id):
    if request.method == "POST":
        name = request.POST['movie_name']
        language= request.POST['language']
        genre= request.POST['genre']
        duration = request.POST['duration']
        img=request.POST['img']
        edit = Details.objects.get(id = id)
        edit.img= img
        edit.movie_name = name
        edit.language=language
        edit.genre= genre
        edit.duration =duration
        edit.save()
        return redirect("/")
    d = Details.objects.get(id = id)
    dict_d = {"d":d}
    return render(request,'update.html',dict_d)

def deleteData(request,id):
    d = Details.objects.get(id = id)
    d.delete()
    return redirect("/")

def Add(request):
    return render(request,'Add.html')


def search_view(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Details.objects.filter(movie_name__icontains=query)
        return render(request, 'search.html', {'form': form, 'results': results})
    else:
        return render(request, 'search.html', {'form': form})


