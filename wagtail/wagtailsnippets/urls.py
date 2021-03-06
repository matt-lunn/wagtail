from django.conf.urls import patterns, url


urlpatterns = patterns(
    'wagtail.wagtailsnippets.views',
    url(r'^$', 'snippets.index', name='wagtailsnippets_index'),

    url(r'^choose/(\w+)/(\w+)/$', 'chooser.choose', name='wagtailsnippets_choose'),
    url(r'^choose/(\w+)/(\w+)/(\d+)/$', 'chooser.chosen', name='wagtailsnippets_chosen'),

    url(r'^(\w+)/(\w+)/$', 'snippets.list', name='wagtailsnippets_list'),
    url(r'^(\w+)/(\w+)/new/$', 'snippets.create', name='wagtailsnippets_create'),
    url(r'^(\w+)/(\w+)/(\d+)/$', 'snippets.edit', name='wagtailsnippets_edit'),
    url(r'^(\w+)/(\w+)/(\d+)/delete/$', 'snippets.delete', name='wagtailsnippets_delete'),
)
