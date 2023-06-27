from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.conf import settings
import os

from django.http import HttpResponseRedirect
from django.contrib.auth. decorators import login_required
from django.contrib.admin.views.decorators import  staff_member_required

from .models import Article, Comment, Images
from .forms import ArticleForm, CommentForm


def article(request, id):
    submitted = False
    form = CommentForm()
    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(article=id)
    images = Images.objects.filter(title=article.title)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.creator = request.user.id 
            comment.article = id 
            comment.save()
            
            messages.success(request, ('Your comment was successfully stored'))
            return HttpResponseRedirect(f"/article/{id}?submitted=True")
    else:
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'article.html', {'article':article,'form': form, 'submitted': submitted,'comments':comments, 'images': images})

@staff_member_required
def delete_article(request, article_id):
    print(article_id)
    article = Article.objects.get(pk=article_id)
    images = Images.objects.filter(title=article.title)
    for image in images:
        print(image.filename())
        image_path = os.path.join(settings.MEDIA_ROOT, 'images\\', image.filename())
        if os.path.exists(image_path):
            os.remove(image_path)

    article.delete()
    images.delete()
    messages.success(request, 'Article deleted successfully.')
    return redirect('/overview/')

@staff_member_required
def delete_image(request, image_id):
    previous_page = request.META.get('HTTP_REFERER')
    image = Images.objects.get(pk=image_id)
    image_path = os.path.join(settings.MEDIA_ROOT, 'images\\', image.filename())
    print(image_path)
    title = image.title
    article = Article.objects.get(title=title)
    article_id = article.id
    if os.path.exists(image_path):
        os.remove(image_path)
    image.delete()
    messages.success(request, 'Image deleted successfully.')
    return redirect(previous_page)

    # image = Images.objects.get(file=image_name)

    # image.delete()
    # messages.success(request, 'Image deleted successfully.')
    

@login_required
def delete_comment(request, comment_id):
    previous_page = request.META.get('HTTP_REFERER')
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment deleted successfully.')
    return redirect(previous_page)


def articles_overview(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    template = loader.get_template('article-overview.html')
    return HttpResponse(template.render(context, request))

# @login_required
# def article_create2(request):
#     article_form = ArticleForm(request.POST or None)
#     context = {
#         'article_form': article_form
#     }

#     if article_form.is_valid():
#         article = article_form.save()
#         context['form'] = ArticleForm()
#         messages.success(request, ('Your article was successfully stored'))
#     else:
#         messages.success(request, ('Your article was not stored'))

#     template = loader.get_template('article-create.html')
#     return HttpResponse(template.render(context, request))


@staff_member_required
def article_create(request):
    submitted = False
    form = ArticleForm()

    if request.method == "POST":
        files = request.FILES.getlist('file')
        for file in files:
            Images.objects.create(file=file, title=request.POST.get('title'))
        form = ArticleForm(request.POST, request.FILES)
        print(request.POST.get('title'))
        if form.is_valid():
            form.save()
            messages.success(request, ('Article was created'))
            return HttpResponseRedirect('/article/create?submitted=True')
        else:
            messages.success(request, ('Something is wrong.'))

    else:
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'article-create.html', {'form': form, 'submitted': submitted})



@staff_member_required
def article_edit(request, article_id):
    article = Article.objects.get(pk=article_id)
    old_title=article.title
    images = Images.objects.filter(title=article.title)
    form = ArticleForm(request.POST or None, instance=article)
    if request.method == "POST":
        files = request.FILES.getlist('file')
        for file in files:
            Images.objects.create(file=file, title=request.POST.get('title'))
        if form.is_valid():
            new_title=form.data.get('title')
            Images.objects.filter(title=old_title).update(title=new_title)
            form.save()
            return redirect('article-overview')
    return render(request,
                  'article-edit.html',
                  {'article': article,
                   'form':form,
                   'images': images}
                  )
