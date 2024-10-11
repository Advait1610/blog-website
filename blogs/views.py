from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import *
from django.db.models import Q

def posts_by_category(request,category_id):
    #fetch the posts that belong to category with id categordy_id
    posts = Blogs.objects.filter(status='published', category=category_id)
    
    #use try/except when we want to do some custom action if category does not exists 
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    # print(posts)

    # use below method when you want to show 404 error page if category not found
    category = get_object_or_404(Category,pk=category_id)

    context =  {
        'posts':posts,
        'category':category
    }
    return render(request,'posts_by_category.html',context)


#blogs
def blogs(request,slug):
    single_post = get_object_or_404(Blogs, slug=slug, status='published' )
    context = {
        'single_post':single_post
    }
    return render(request,'blogs.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) , status = 'published' )
    content = {
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request, 'search.html',content)