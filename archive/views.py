
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from models import *
#from forms import BlogPostForm

def index(request, slug=None, template_name='archive/index.html'):
    users = User.objects
    template_context = {'users': users}
    #print posts[0].get_absolute_url()
    return render_to_response(
        template_name,
        template_context,
        RequestContext(request)
    )

def match(request, slug=None, template_name='archive/match.html'):
    matchs = Match.objects
    template_context = {'matchs': matchs}
    #print posts[0].get_absolute_url()
    return render_to_response(
        template_name,
        template_context,
        RequestContext(request)
    )


def user(request, slug, template_name='archive/match.html'):
    u = User.objects.get(username=slug)
    matchs = Match.objects( Q(winner=u) | Q(loser=u) )

    template_context = {'matchs': matchs}
    return render_to_response(
        template_name,
        template_context,
        RequestContext(request)
    )



def editmatch(request, slug, template_name='archive/match.html'):
    m = Match.objects.get(id=slug)
    m_data = { 'winner': m.winner.username
            ,'loser': m.loser.username
            ,'winscore': m.winscore
            ,'losescore': m.losescore
            ,'matchlength': m.matchlength
            ,'tags': ','.join(m.tags)
            ,'loserER': m.loserER
            ,'loserPR': m.loserPR
            ,'loserPR': m.loserPR
            ,'winnerER': m.winnerER
            ,'mid' : slug
    }
    form = MatchForm(m_data)
    return render_to_response('archive/newmatch.html', {
        'form': form,
    })



def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            #subject = form.cleaned_data['subject']
            #message = form.cleaned_data['message']
            #sender = form.cleaned_data['sender']
            #cc_myself = form.cleaned_data['cc_myself']
            usr = User(username=form.cleaned_data['username'])
            usr.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('archive/contact.html', {
        'form': form,
    })



def newmatch(request):
    if request.method == 'POST': # If the form has been submitted...
        form = MatchForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid():
            #subject = form.cleaned_data['subject']
            #message = form.cleaned_data['message']
            #sender = form.cleaned_data['sender']
            #cc_myself = form.cleaned_data['cc_myself']
            if form.cleaned_data['mid'] == '69':
                m = Match(
                winner= doUser( form.cleaned_data['winner'].lower()  )
                ,loser= doUser( form.cleaned_data['loser'].lower() )
                ,winscore = form.cleaned_data['winscore']
                ,losescore = form.cleaned_data['losescore']
                ,matchlength = form.cleaned_data['matchlength']
                ,tags = form.cleaned_data['tags'].split(',')
                #,matfile = request.FILES['matfile']
                )
                if request.FILES.has_key('matfile'):
                    m.matfile = 'True'
                m.save()
                handle_uploaded_file( request.FILES['matfile'] , str(m.id) )

            else:
                m = Match.objects.get(id=form.cleaned_data['mid'])
                m.winner = doUser( form.cleaned_data['winner'].lower() )
                m.loser= doUser( form.cleaned_data['loser'].lower() )
                m.winscore = form.cleaned_data['winscore']
                m.losescore = form.cleaned_data['losescore']
                m.matchlength = form.cleaned_data['matchlength']
                m.tags = form.cleaned_data['tags'].split(',')
                m.save()

            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = MatchForm() # An unbound form
        form.is_multipart()
    return render_to_response('archive/newmatch.html', {
        'form': form,
    })









"""

def new(request, template_name='archive/new_or_edit.html'):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/")
    else:
        form = BlogPostForm()

    template_context = {'form': form}

    return render_to_response(
        template_name,
        template_context,
        RequestContext(request)
    )


def show(request, slug, template_name='blog/show.html'):
    post = BlogPost.objects.get(slug=slug)
    template_context = {'post': post}

    return render_to_response(
        template_name,
        template_context,
        RequestContext(request)
    )



def delete(request, slug):
    post = BlogPost.objects(slug=slug)
    post.delete()
    return HttpResponseRedirect("/")

def edit(request, slug, template_name='blog/new_or_edit.html'):

    post = BlogPost.objects.get(slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = BlogPostForm(instance=post)

    template_context = {'form': form}

    return render_to_response(
        template_name,
        template_context,
        RequestContext(request)
    )
"""
