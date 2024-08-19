from django.shortcuts import render

from django.views import View
import requests


class HomeView(View):
    def get(self, request):
        services=requests.get("http://localhost:8000/api/services").json()
        blogs = requests.get("http://localhost:8000/api/blogs").json()
        advisors = requests.get("http://localhost:8000/api/advisors").json()
        authors = requests.get("http://localhost:8000/api/authors").json()
        reviews = requests.get("http://localhost:8000/api/reviews").json()

        context={'services':services
                 ,'blogs':blogs
                 ,'advisors':advisors
                 ,'authors':authors
                 ,'reviews':reviews}

        return render(request, 'index.html',context)




class ServicesView(View):
    def get(self, request):
        services=requests.get("http://localhost:8000/api/services").json()
        reviews = requests.get("http://localhost:8000/api/reviews").json()
        context={'services':services,
                 'reviews': reviews
                 }
        return render(request,'service.html',context)


def service_detail_view(request,id):
    response = requests.get(f"http://localhost:8000/api/services/{id}/")
    service = response.json()
    return render(request, 'service-detail.html', {'service': service})








class BlogView(View):
    def get(self, request):
        blogs=requests.get("http://localhost:8000/api/blogs").json()
        context={'blogs':blogs}
        return render(request,'blog.html',context)


class AdvisorsView(View):
    def get(self, request):
        advisors=requests.get("http://localhost:8000/api/advisors").json()
        authors=requests.get("http://localhost:8000/api/authors").json()
        context={'advisors':advisors,
                 'authors':authors}
        return render(request,'team.html',context)

class ReviewsView(View):
    def get(self, request):
        reviews=requests.get("http://localhost:8000/api/reviews").json()
        context={'reviews':reviews}
        return render(request,'testimonial.html',context)


def about_view(request):
    return render(request, 'about.html')

def feature_view(request):
    return render(request, 'feature.html')



def contact_view(request):
    return render(request, 'contact.html')




