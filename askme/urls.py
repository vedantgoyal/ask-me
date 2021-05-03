from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views
from askme.views import MyOwnView

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    url(r'^my-own-view/$', MyOwnView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]