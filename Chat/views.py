from django.shortcuts import render

# Create your views here.



def profile(request):
    username = request.GET.get('username')
    return render(request, 'profile.html')