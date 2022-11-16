# from sys import path

# from django.urls import include,re_path
# from rest_framework.urlpatterns import format_suffix_patterns
# from register import views
# from django.conf.urls import url
# from django.contrib import admin

# from rest_framework import routers
# router = routers.DefaultRouter()



# router.register('user_details', views.UserDetail)
# urlpatterns = [path('api/', include(router.urls)), ...]
# urlpatterns = [

#     re_path(r'^admin/', admin.site.urls),
#     re_path(r'^User_details/', views.ListUserViews.as_view()),
#     re_path(r'^User_details/(?P<pk>[0-9]+)/', views.UserDetail.as_view()),

# ]
# urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path
from register import views

urlpatterns = [
	path('/', views.ListUserViews.as_view()),
	path('/<int:id>', views.ListUserViews.as_view()),
	]