from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class DisplayTable(APIView):
    def get(self, request):
        return render(request, 'template_1.html', {})
