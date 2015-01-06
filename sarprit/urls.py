from django.conf.urls import patterns, include, url
from django.contrib import admin

import survey.urls
import classifiers.urls
import rootword.urls

def twitter(request):
	from django.shortcuts import render
	return render(request, 'twitter/index.html')

def review_save(request, id, flag):
	from survey.models import Review
	from django.http import JsonResponse

	review = Review.objects.get(id=int(id))
	review.flag = int(flag)
	review.save()
	return {'id':id}

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^classify/', include(classifiers.urls)),
    url(r'^reviews/', "survey.views.reviews_table"),
    url(r'^rootword/', include(rootword.urls)),
    url(r'', include(survey.urls)),
    url(r'^twitter/', twitter),
    url(r'^review/save/(?P<id>\d+)/(?P<flag>\d)', review_save)
)
