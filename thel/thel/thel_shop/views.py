from django.shortcuts import render
from .models import Clothes, Category
from django.views.generic import ListView, DetailView


class Category(ListView):
    model = Clothes
    template_name = 'category.html'
    context_object_name = 'clothes'

    def get_queryset(self):
        return Clothes.objects.filter(is_published=True)


class Get_category(ListView):
    model = Category
    template_name = 'one_category.html' 
    context_object_name = 'clothes'  
    allow_empty = False     

    def get_queryset(self):
        return Clothes.objects.filter(category_id = self.kwargs['category_id'], is_published=True)


class Clothe_detail(DetailView):
    model = Clothes
    template_name = 'clothe_detail.html' 
    context_object_name = 'clothe_detail'

def main(request):
    return render(request, 'main.html')

def faq(request):
    return render(request, 'faq.html') 

def thel_society(request):
    return render(request, 'thel_society.html') 

def about_us(request):
    return render(request, 'about_us.html')         
    

