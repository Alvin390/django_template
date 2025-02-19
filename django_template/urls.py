from alvin_django_template.urls import path
from django_template import views

urlpatterns = [
    path('', views.index, name='my_home'),
    path('about/', views.about, name='my_about'),
    path('contact/', views.contact, name='my_contact'),
    path('products/', views.products, name='my_products'),
    path('services/', views.single_product, name='single_product'),

]