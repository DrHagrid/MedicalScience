# -*- coding: utf-8 -*-
from django.shortcuts import render
from reference.models import ArticleSection, Article, Picture


def reference_choice(request):
    article_sections = ArticleSection.objects.all()
    article_section_list = list()
    for article_section in article_sections:
        articles = Article.objects.filter(section=article_section).filter(is_active=True)
        article_section_list.append({'section': article_section, 'articles': articles, 'count': len(articles)})
    return render(request, 'reference/reference_choice.html', locals())


def reference(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'reference/reference.html', locals())


def about(request):
    return render(request, 'reference/about.html', locals())