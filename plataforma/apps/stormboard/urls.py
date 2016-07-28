from django.conf import settings
from django.conf.urls import patterns, include, url

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.views.generic.base import TemplateView


admin.autodiscover()

api = [

]

urlpatterns = [  # User management

                 url(r'^tos/$', TemplateView.as_view(template_name='stormboard/users/tos.html'), name="tos"),
                 url(r'^tour/$', TemplateView.as_view(template_name='stormboard/tour.html'), name="tour"),
                 url(r'^pricing/$', TemplateView.as_view(template_name='stormboard//main/pricing.html'),
                     name="pricing"),

                 url(r'^pricing_edu/$', TemplateView.as_view(template_name='stormboard//main/pricing_edu.html'),
                     name="pricing_edu"),

                 url(r'^help/$', TemplateView.as_view(template_name='stormboard/main/help.html'), name="help"),
                 url(r'^browsers/$', TemplateView.as_view(template_name='stormboard/main/browsers.html'),
                     name="browsers"),
                 url(r'^privacy/$', TemplateView.as_view(template_name='stormboard/main/privacy.html'), name="privacy"),

                 url(r'^about/$', TemplateView.as_view(template_name='stormboard/main/about.html'), name="about"),
                 url(r'^contact/$', TemplateView.as_view(template_name='stormboard/main/contact.html'), name="contact"),
                 url(r'^press/$', TemplateView.as_view(template_name='stormboard/press.html'), name="press"),

                 url(r'^$', TemplateView.as_view(template_name='stormboard/index.html'), name="index"),

                 url(r'^api/', include(api, namespace='api'))
]

urlpatterns += staticfiles_urlpatterns()