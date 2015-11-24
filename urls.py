from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = (
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name='logout'),
    # url(r'^password-reset/$', 'django.contrib.auth.views.password_reset',
    #     {'template_name': 'password_reset.html'}, name='password_reset'),
    # url(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done',
    #     {'template_name': 'password_reset_done.html'}, name='password_reset_done'),
    # url(r'^password-reset/confirm/(?P<uidb64>.*)/(?P<token>.*)/$', 'django.contrib.auth.views.password_reset_confirm',
    #     {'template_name': 'password_reset_confirm.html'}, name='password_reset_confirm'),
    # url(r'^password-reset/complete/', 'django.contrib.auth.views.password_reset_complete',
    #     {'template_name': 'password_reset_complete.html'}, name='password_reset_complete'),

    url(r'^register/$', 'ask.views.register_user', name='register'),
    url(r'^register/done/$', 'ask.views.register_done', name='register_done'),

    url(r'^$', 'ask.views.home_view', name='home'),
    url(r'^poll/(?P<poll_id>\d+)/$', 'ask.views.poll_view', name='poll'),
    url(r'^poll/(?P<poll_id>\d+)/(?P<question_id>\d+)/$', 'ask.views.poll_view', name='poll_question'),
    url(r'^answer/(?P<poll_id>\d+)/(?P<question_id>\d+)/$', 'ask.views.answer_process', name='answer'),
    url(r'^poll/(?P<poll_id>\d+)/done/$', 'ask.views.poll_done_view', name='poll_done'),
    url(r'^payouts/$', 'ask.views.payouts_view', name='payouts'),
    url(r'^settings/$', 'ask.views.settings_view', name='settings'),
)
