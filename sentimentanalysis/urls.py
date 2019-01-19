

from django.conf.urls import url
from . import SAviews

app_name = 'sentimentanalysis'

urlpatterns = [
    url(r'^$', SAviews.IndexView.as_view(), name="index"),
]
