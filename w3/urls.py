"""Defines URL patterns for w3 app."""
from django.conf.urls import url
from . import views

urlpatterns = [
    # work page
    #url(r'^$', 
    #    views.sbsbook, 
    #    name='sbsbook'),

    # Home page
    url(r'^$', 
        views.index, 
        name='index'),

    url(r'^contact$', 
        views.contact, 
        name='contact'),

    url(r'^employer$', 
        views.employer, 
        name='employer'),

    url(r'^install_Ins$', 
        views.install_Ins, 
        name='install_Ins'),

    url(r'^kws$',
        views.kws,
        name='kws'),

    # Show all topics
    url(r'^topics/$', 
        views.topics, 
        name='topics'),

    # Detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', 
        views.topic, 
        name='topic'),

    # Page for adding a new topic
    url(r'^new_topic/$', 
        views.new_topic, 
        name='new_topic'),

    # page for adding a new entry
    url(r'^new_entry/(?P<topic_id>\d+)/$', 
            views.new_entry, 
            name='new_entry'),

    # Page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', 
            views.edit_entry,
            name='edit_entry'),


]