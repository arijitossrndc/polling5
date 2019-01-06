
from django.contrib import admin
from django.urls import include, path
from.import polls.views

app_name  = 'polls'
admin.autodiscover()

urlpatterns = [
    path('', polls.views.IndexView.as_view(), name='index'),
    path('<int:pk>/',polls.views.DetailView.as_view(),name='detail'),
    path('<int:pk>/results/',polls.views.ResultsView.as_view(),name='results'),
    path('<int:question_id>/vote/',polls.views.vote,name='vote'),
    path('admin/', admin.site.urls),
]
