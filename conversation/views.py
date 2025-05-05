from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from item.models import Item
from .models import Conversation, Message
from .forms import MessageForm


# Create your views here.

@login_required(login_url="login")
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    context = {'conversations': conversations}
    return render(request, 'conversation/inbox.html', context)


@login_required(login_url='login')
def new(request, id):
    item = Item.objects.get(pk=id)

    conversation = Conversation.objects.filter(item=item).filter(members__in=[request.user.id]).first()

    if request.method == 'POST':
        message = MessageForm(request.POST)
        if message.is_valid():
            if not conversation:
                conversation = Conversation.objects.create(item=item)
                conversation.members.add(request.user.id)
                conversation.members.add(item.created_by)
                conversation.save()

            conversation_message = message.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.user = request.user
            conversation_message.save()

            return redirect('conversation:chat', conversation.id)

    context = {
        'item': item
    }

    return render(request, 'conversation/inbox.html', context)


def chat(request, id):
    conversation = Conversation.objects.get(pk=id)
    product = conversation.item
    message_form = MessageForm()
    conversation_messages = Message.objects.filter(conversation=conversation)

    return render(request, 'conversation/chat.html',
                  {'conversation': conversation, 'conversation_messages': conversation_messages, 'product': product,
                   'message_form': message_form})
