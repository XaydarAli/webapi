from django.urls import path
from .views import HomeView,about_view,ServicesView,BlogView,AdvisorsView,feature_view,contact_view,ReviewsView,service_detail_view
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('services/', ServicesView.as_view(), name='service'),
    path('services/<int:id>/', service_detail_view, name='service-detail'),
    path('blogs/', BlogView.as_view(), name='blog'),
    path('reviews/', ReviewsView.as_view(), name='reviews'),
    path('about/', about_view, name='about'),
    path('advisors/', AdvisorsView.as_view(), name='team'),
    path('feature/', feature_view, name='feature'),
    path('contact/', contact_view, name='contact'),

]