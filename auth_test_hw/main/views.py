from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'main/index.html')

@login_required
def profile(request):
    return render(request, 'main/profile.html', {'user': request.user})

