from django.urls import path
from home import views
from .views import team, testimonials, blog

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('blog/',blog.as_view(),name='blog'),
    path('blog-details/',views.blog_details, name='blog-details'),
    path('contact/',views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('pricing/', views.pricing, name='pricing'),
    path('service-details/', views.service_details, name='service-details'),
    path('services/', views.services, name='services'),
    path('starter-page/', views.starter_page, name='starter-page'),
    path('team/', team.as_view(), name='team'),
    path('testimonials/', testimonials.as_view(), name='testimonials'),
]