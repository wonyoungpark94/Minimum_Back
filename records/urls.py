from django.urls import path
from records.views import get_records
urlpatterns = [
        path('', get_records )

]
