# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404


# Create your views here.
def home_page(request):
    context = {}
    project_list = Project.objects.filter(main_page=True)
    review_list = ClientReview.objects.filter(main_page=True)
    client_list = Client.objects.filter(active=True)
    content = SiteContent.objects.filter(active=True)
    if content.exists():
        context['content'] = content.latest('pk')
    context['project_list'] = project_list
    context['review_list'] = review_list
    context['client_list'] = client_list
