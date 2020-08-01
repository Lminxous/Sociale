from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PostCreateForm,CommentCreateForm
from .models import Post,Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def dummy(request):
    pass


# Home

def home(request):
    posts_list = Post.objects.all().order_by('-date_posted')
    page = request.GET.get('page', 1)

    paginator = Paginator(posts_list, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts' : posts ,
    }
    return render(request,'social/home.html',context)


def user_post_view(request,username):
    user = get_object_or_404(User,username=username)
    posts = Post.objects.filter(author=user).order_by('-date_posted')


    context = {
        'posts' : posts ,
        'user' :user,
    }
    return render(request,'social/user-detail.html',context)    

# def user_post_view(request,username):
#     user = get_object_or_404(User,username=username)
#     posts = Post.objects.filter(author=user).order_by('-date_posted')

#     page = request.GET.get('page', 1)

#     paginator = Paginator(posts, 5)
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)

#     context = {
#         'posts' : posts ,
#         'user' :user,
#     }
#     return render(request,'social/user-detail.html',context)



# Creating,Updating & Deleting Posts

@login_required    
def post_create_view(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            post = Post(title=title,content=content,author=request.user)
            post.save()
            print(messages.success(request,'New post has been created.'))
            return redirect('social-home')
    else:
        form = PostCreateForm(instance=request.user)
    return render(request,'social/post-create.html',{'form':form})    


@login_required
def post_update_view(request,id):
    post = Post.objects.get(id=id)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostCreateForm(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                post.title = request.POST["title"]
                post.content = request.POST["content"]
                post.save() 

                messages.info(
                     request, f'Post "{post.title}" has been successfully updated.'
                )
                return redirect("social-home")
        else:
            form = PostCreateForm({"title": post.title, "content": post.content})
    else:
        return HttpResponse(
            "<h1>You can't update a post written by someone else, If you have staff access use admin site.</h1>"
        )
    return render(request, "social/post-update.html", {"form": form})    

         
@login_required
def post_delete_view(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post": post
    }
    if request.user == post.author:
        if request.method == "POST":
            messages.warning(
                request, f'Post "{post.title}" has been successfully deleted.'
            )
            post.delete()
            return redirect("social-home")
    else:
        return HttpResponse(
            "<h1>You can't delete a post written by others, If you have administrative access kindly use admin site.</h1>"
        )
    return render(request, "social/post-confirm-delete.html", context)

@login_required
def post_report_view(request,id):
    post = Post.objects.get(id=id)
    context = {
        "post": post
    }

    if request.method == "POST" and post.author != request.user: 
        if request.user not in post.reported_by.all():
            post.reported_by.add(request.user)
            post.save()
            if post.reported_by.count() > 1:
                messages.warning(
                    request, f'Post "{post.title}" has been successfully deleted.'
                )
                post.delete()  
            else:
                messages.warning(
                request, f'Post "{post.title}" has been successfully reported {post.reported_by.count()} times')          
        else:
            messages.warning(
                    request, f'Post "{post.title}" has been already reported by you.'
                )
        return redirect("social-home")   
    return render(request, "social/post-report.html", context)        




# Creating,Updating & Deleting Comments

@login_required
def post_detail_view(request, id):
    post = Post.objects.get(id=id)
    form = CommentCreateForm(instance=request.user)

    if request.method == "POST":

        if 'Post' in request.POST:
            form = CommentCreateForm(request.POST,instance=request.user)
            if form.is_valid(): 
                form.save()
                com = Comment(  comment=request.POST["comment"],
                                author=request.user,
                                post=post  )
                com.save()  
                messages.success(
                     request, f'Your comment "{com.comment}" for  post "{com.post}" has been added successfully.'
                ) 

    else:
            form

    context = {
        "post" : post,
        "comments": Comment.objects.filter(post=post),
        "form" : form,
    }    

    return render(request, "social/post-detail.html", context)     


@login_required
def comment_update_view(request,id):
    com = Comment.objects.get(id=id)
    if request.user == com.author:
        if request.method == 'POST':
            form = CommentCreateForm(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                com.comment = request.POST["comment"]
                # com.save() 
                # com = Comment(comment=request.POST["comment"],
                #       author=request.user)
                com.save()

                messages.info(
                     request, f'Your comment "{com.comment}" for  post "{com.post}" has been successfully updated.'
                )
                return redirect("social-home")
                
        else:
            form = CommentCreateForm(instance=request.user)
    else:
        return HttpResponse(
            "<h1>You can't update a comment written by someone else, If you have staff access use admin site.</h1>"
        )
    return render(request, "social/comment-update.html", {"form": form})    


@login_required
def comment_delete_view(request,id):
    com = Comment.objects.get(id=id)
    context = {
        "com": com
    }
    if request.user == com.author:
        if request.method == 'POST':
            messages.warning(request, f'Comment {com.comment} for {com.post} has been successfully deleted.')
            com.delete()    
            return redirect('social-home')

    else:
        return HttpResponse(
            "<h1>You can't delete a post written by someone else, If you have staff access use admin site.</h1>"
        )
    return render(request, "social/comment-confirm-delete.html",context)        
       
    






# @login_required
# def post_detail_view(request, id):
#     post = Post.objects.get(id = id)
#     form = CommentCreateForm(instance=request.user)


# # Managing Multiple post requests on a single page

#     if request.method == "POST":

#         if 'Post' in request.POST:
#             form = CommentCreateForm(request.POST,instance=request.user)
#             if form.is_valid(): 
#                 form.save()
#                 com = Comment(  comment=request.POST["comment"],
#                                 author=request.user,
#                                 post=post  )
#                 com.save()

#         elif 'Edit' in request.POST:
#             form = CommentCreateForm(request.POST,instance=request.user)
#             if form.is_valid(): 
#                 form.save()
#                 com = Comment(  comment=request.POST["comment"],
#                                 author=request.user,
#                                 post=post  )
#                 com.save()
                            
#         elif 'Delete' in request.POST:
#             com = Comment.objects.filter(comment=request.POST["comment"]).first()
#             messages.warning(request, f'Comment {com.comment} has been successfully deleted.')
#             com.delete()       

#     else:
#             form

#     context = {
#         "post" : post,
#         "comments": Comment.objects.filter(post=post),
#         "form" : form,
#     }    

#     return render(request, "social/post-detail.html", context)     

