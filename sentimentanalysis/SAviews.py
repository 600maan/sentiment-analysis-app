from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import generic
import sentimentanalysis.sentiment_mod as s


class IndexView(generic.ListView):
    template_name = 'sentimentanalysis/index.html'
    def get_queryset(self):
        return ""

class SentimentAnalysis(APIView):

    def post(self, request):
        text = str(request.POST.get('param'))
        result = s.sentiment(text)
        return Response(result)