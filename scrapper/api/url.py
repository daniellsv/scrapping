from django.urls import path
from .api import diarioAS_api_view, diarioAs_detail_view


urlpatterns = [
    path('scrapper/', diarioAS_api_view, name='diarioAS_api_view'),
    path('scrapper/<str:name>', diarioAs_detail_view, name='diarioAs_detail_view'),

]