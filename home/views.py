from django.shortcuts import render
from .models import Team, Testimonial, Blog
from django.views.generic import ListView

# Create your views here.
def home(request):
    return render(request, 'index.html')

class blog(ListView):
    model = Blog
    template_name = 'blog.html/'
    context_object_name = 'blogs'
    
def blog_details(request):
    return render(request, 'blog-details.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def pricing(request):
    return render(request, 'pricing.html')

def service_details(request):
    return render(request, 'service-details.html')

def services(request):
    return render(request, 'services.html')

def starter_page(request):
    return render(request, 'starter-page.html')

class team(ListView):
    model = Team
    template_name = 'team.html/'
    context_object_name = 'teams'

class testimonials(ListView):
    model = Testimonial
    template_name = 'testimonials.html/'
    context_object_name = 'testimonials'

def about(request):
    return render(request, 'about.html')