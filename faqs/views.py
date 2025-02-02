from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from django.http import JsonResponse

class FAQList(APIView):
    def get(self, request, format=None):
        lang = request.GET.get('lang', 'en')  # Default  English
        faqs = FAQ.objects.all()

        # Retrieve the appropriate question translation based on the language query parameter
        faq_data = []
        for faq in faqs:
            if lang == 'hi':
                faq_data.append({'question': faq.question_hi or faq.question, 'answer': faq.answer})
            elif lang == 'bn':
                faq_data.append({'question': faq.question_bn or faq.question, 'answer': faq.answer})
            else:
                faq_data.append({'question': faq.question, 'answer': faq.answer})

        return JsonResponse(faq_data, safe=False)
