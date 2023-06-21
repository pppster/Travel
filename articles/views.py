from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.contrib.auth. decorators import login_required

from .models import Article
from .forms import ArticleForm

def article(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article,
    }
    template = loader.get_template('article.html')
    return HttpResponse(template.render(context, request))


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
    form = ArticleForm()  # Instantiate the form before the conditional block

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/creation?submitted=True')
    else:
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'article-create.html', {'form': form, 'submitted': submitted})