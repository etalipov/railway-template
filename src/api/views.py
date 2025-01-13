from django.http import HttpResponse
from django.views import View


class TestView(View):
    @staticmethod
    def get(request):
        return HttpResponse("Hello, World!")
