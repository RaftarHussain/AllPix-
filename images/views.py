from django.shortcuts import render,redirect,get_object_or_404
from .models import Image,Category
from django.db.models import Q

# Create your views here.

def home(request):
    categories = Category.objects.all()
    
    return render(request,'gallery/home.html',{'categories':categories})

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Image.objects.filter(
            Q(title__icontains=query)  | Q(category__name__icontains=query)
        ).distinct()
    return render(request,'gallery/search.html',{"results":results,'query':query})

    

def category_detail(request,slug):
    category = get_object_or_404(Category,slug=slug)
    images = category.images.all()
    context = {
        "category":category,
        "images":images,
    }
    return render(request,'gallery/category_detail.html',context)


def image_detail(request,pk):
    image = get_object_or_404(Image,pk=pk)
    return render(request,"gallery/image_detail.html",{"image":image})
