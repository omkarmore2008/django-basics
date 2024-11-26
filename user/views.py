from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

class AudioWebSocketView(View):
    def get(self, request):
        # You can add context data if needed
        return render(request, 'index.html')