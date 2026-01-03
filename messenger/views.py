from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import MessageForm
from .models import Message


@login_required
def send_message(request):
    """
    Enviar mensaje:
    - sender = request.user
    - is_read arranca en False
    """
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.is_read = False
            msg.save()
            return redirect("inbox")
    else:
        form = MessageForm()

    return render(request, "messenger/message_form.html", {"form": form})


@login_required
def inbox(request):
    # Bandeja de entrada: mensajes recibidos por el usuario logueado.
    inbox_messages = Message.objects.filter(recipient=request.user).order_by("-created_at")
    return render(request, "messenger/inbox.html", {"inbox_messages": inbox_messages})


@login_required
def outbox(request):
    # Enviados: mensajes enviados por el usuario logueado.
    sent_messages = Message.objects.filter(sender=request.user).order_by("-created_at")
    return render(request, "messenger/outbox.html", {"sent_messages": sent_messages})


@login_required
def message_detail(request, pk):
    """
    Detalle de un mensaje.
    Seguridad: solo puede verlo el sender o el recipient.
    Si el usuario es el recipient, se marca como leído.
    """
    msg = get_object_or_404(Message, pk=pk)

    if msg.sender != request.user and msg.recipient != request.user:
        # si no sos ni emisor ni receptor, te mandamos al inbox
        return redirect("inbox")

    # marcar leído solo si lo abrió el receptor
    if msg.recipient == request.user and not msg.is_read:
        msg.is_read = True
        msg.save()

    return render(request, "messenger/message_detail.html", {"msg": msg})
