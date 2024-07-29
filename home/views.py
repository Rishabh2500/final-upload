from django.http import HttpResponse


from rest_framework.views import APIView  
from rest_framework.response import Response  
from django.shortcuts import render  
from rest_framework import status 

# Create your views here.

## First Create API
class StudentView(APIView):  
    
    def get(self, request, *args, **kwargs):  
        
        str1 = ""

        f = open("D:\Seats.sql", "r")
        for x in f:
            str1 += x

        return Response({'status': 'success', "Names" : str1}, status=200) 
    

    def post(self, request):  
        data=request.data
        print("New Student Request : ", data.get('data'))
        f = open("D:\Seats.sql", "a")
        f.write(data.get('data'))
        f.close()
        return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)


def index(request):
    context={                 # to fetch something
        "variable": "this is sent"
    }
    return render(request, 'index.html',context)
    # return HttpResponse("This is homepage")

def movies(request):
    # return HttpResponse("This is moviespage")
    return render(request, 'movies.html')

def streams(request):
    # return HttpResponse("This is straemspage")
    return render(request, 'streams.html')

def events(request):
    # return HttpResponse("This is eventspage")
    return render(request, 'events.html')

def plays(request):
    # return HttpResponse("This is playspage")
    return render(request, 'plays.html')

def sports(request):
    # return HttpResponse("This is sportspage")
    return render(request, 'sports.html')  