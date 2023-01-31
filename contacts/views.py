import json
from django.http import JsonResponse, HttpResponse
from rest_framework.exceptions import ValidationError
from django.views import View
from .models import Contact
from .serizalizer import ContactSerializer

class ContactDetailsView(View):

    def get(self, request, contact_id):
        contact = Contact.objects.get(id=contact_id)
        return JsonResponse(data=ContactSerializer(contact).data)


class ContactCreateView(View):

    def post(self, request):
        data = json.loads(request.body)
        if "first_name" not in data: raise ValidationError("first_name is a required field")
        if "phone" not in data: raise ValidationError("phone is a required field")

        contact = Contact.objects.create(
            first_name = data["first_name"],
            last_name = data["last_name"] if "last_name" in data else None,
            company_name = data["company_name"] if "company_name" in data else None,
            email = data["email"] if "email" in data else None,
            phone = data["phone"]
        )

        return JsonResponse(data=ContactSerializer(contact).data)

    