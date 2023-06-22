from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.contrib.auth. decorators import login_required

from .models import Article
from .forms import ArticleForm, CommentForm


def article(request, id):
    submitted = False
    form = CommentForm()
    article = Article.objects.get(id=id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.creator = request.user.id # logged in user
            comment.save()
            
            messages.success(request, ('Your comment was successfully stored'))
            return HttpResponseRedirect(f"/article/{id}?submitted=True")
    else:
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'article.html', {'article':article,'form': form, 'submitted': submitted})



def articles_overview(request):
    articles = Article.objects.all().values()
    context = {
        'articles': articles
    }

    template = loader.get_template('article-overview.html')
    return HttpResponse(template.render(context, request))

@login_required
def article_create2(request):
    article_form = ArticleForm(request.POST or None)
    context = {
        'article_form': article_form
    }

    if article_form.is_valid():
        article = article_form.save()
        context['form'] = ArticleForm()
        messages.success(request, ('Your article was successfully stored'))
    else:
        messages.success(request, ('Your article was not stored'))

    template = loader.get_template('article-create.html')
    return HttpResponse(template.render(context, request))


@login_required
def article_create(request):
    submitted = False
    form = ArticleForm()

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/article/create?submitted=True')
        else:
            messages.success(request, ('Something is wrong.'))

    else:
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'article-create.html', {'form': form, 'submitted': submitted})



@login_required
def article_edit(request, article_id):
    article = Article.objects.get(pk=article_id)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('article-overview')
    return render(request,
                  'article-edit.html',
                  {'article': article,
                   'form':form}
                  )
