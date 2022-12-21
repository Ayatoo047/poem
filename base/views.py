from django.shortcuts import render, redirect
from .models import Poems, Message
from .forms import PoemForm

# Create your views here.
def poems(request):
    page = 'poems'
    poems = Poems.objects.all()

    context = {"poems":poems, 'page': page}
    return render(request, "base/poems.html", context)

def allpoems(request):
    poems = Poems.objects.all()

    context = {"poems":poems}
    return render(request, "base/allpoems.html", context)    

def poem(request, pk):
    poem = Poems.objects.get(id=pk)

    context = {"poem":poem}
    return render(request, "base/poem.html", context)


def about(request):
    poems = Poems.objects.all()

    context = {'poems': poems}
    return render(request, "about-me.html", context)


def newPoem(request):
    # form = PoemForm()
    poems = Poems.objects.all()
    number = poems.count()

    if request.method == 'POST':
        image = request.FILES.get('image')
        description = request.POST['description']
        title = request.POST['title']


        newpoem = Poems.objects.create(
            featured_image = image,
            title = title,
            description = description,
            index = number+1
        )
        newpoem.save()
        # pn = newpoem.index - 1

        return redirect('create')
    context = {'number': number,}
    return render(request, 'base/create.html', context)


def delete(request, pk):
    poem = Poems.objects.get(id=pk)
    if request.method == "POST":
        poem.delete()
        return redirect('poems')

    context = {'poem': poem}
    return render(request, 'base/delete.html', context)


def contact(request):
    poems = Poems.objects.all()

    if request.method == 'POST':
        body = request.POST['message']
        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']

        newmessage = Message.objects.create(
            body = body,
            subject = subject,
            name = name,
            email = email,
        )
        newmessage.save()

    context = {'poems': poems}
    return render(request, 'base/contact.html', context)


def inbox(request):
    allmessages = Message.objects.all()
    unread = allmessages.filter(is_read=False).count()
    context = {"allmessages": allmessages, 'unread': unread}
    return render(request, 'base/inbox.html', context)

def messagers(request, pk):
    singlemessage = Message.objects.get(id=pk)
    if singlemessage.is_read == False:
        singlemessage.is_read = True
        singlemessage.save()
    # unreadNumber = userinbox.filter(is_read=False).count()
    page = 'messengers'

    context = {'singlemessage': singlemessage}
    return render(request, 'base/message.html', context)


def updatePoem(request, pk):
    poem = Poems.objects.get(id=pk)
    form = PoemForm(instance=poem)

    if request.method == "POST":
        form = PoemForm(request.POST, instance=poem)
        if form.is_valid:
            form.save()
            return redirect("poems")

    context = {'form': form, "poem": poem}
    return render(request, 'base/create.html', context)