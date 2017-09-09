from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'backend.views.home', name='home'),
                       url(r'^test$', 'backend.views.test', name='test'),
                       url(r'^testview$', 'backend.views.testview', name='testview'),
)
