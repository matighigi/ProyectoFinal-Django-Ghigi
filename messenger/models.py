from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """
    Mensaje entre usuarios.
    - sender: quien envía
    - recipient: quien recibe
    - subject: asunto corto
    - body: contenido
    - created_at: fecha/hora
    - is_read: marca simple de leído/no leído
    """
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_messages",
    )
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_messages",
    )

    subject = models.CharField(max_length=120, blank=True)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"De {self.sender.username} para {self.recipient.username} ({self.created_at:%Y-%m-%d})"
