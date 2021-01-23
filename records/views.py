
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from records.models import WeightRecord
import json
# Create your views here.

@api_view(["GET"])
def get_records(request):
    data = WeightRecord.objects.all()
    for datum in data:
        print(datum.__dict__)
    return Response(data={})