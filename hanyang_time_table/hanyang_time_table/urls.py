from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'', include('hanyang_time_table.courses.urls')),
    # Examples:
    # url(r'^$', 'hanyang_time_table.views.home', name='home'),
    # url(r'^hanyang_time_table/', include('hanyang_time_table.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
