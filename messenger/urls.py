from django.urls import path
from .views import send_message, inbox, outbox, message_detail

urlpatterns = [
    path("", inbox, name="inbox"),                 # /messages/
    path("sent/", outbox, name="outbox"),          # /messages/sent/
    path("send/", send_message, name="send_message"),  # /messages/send/
    path("<int:pk>/", message_detail, name="message_detail"),  # /messages/1/
]
