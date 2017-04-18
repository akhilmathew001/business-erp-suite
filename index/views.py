from django.shortcuts import render

# Create your views here.

def get_index_view(request):
    return render(request, 'index/index.html')
