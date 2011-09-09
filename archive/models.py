
from mongoengine import *
import datetime
from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(max_length=100,required=False)
    firstname = forms.CharField()
    lastname = forms.CharField()
    #rating = forms.BooleanField(required=False)


class MatchForm(forms.Form):
    mid= forms.CharField(initial='69', widget=forms.widgets.HiddenInput())
    winner = forms.CharField(max_length=100)
    loser = forms.CharField(max_length=100)
    winscore = forms.IntegerField()
    losescore = forms.IntegerField()
    matchlength = forms.IntegerField()
    winnerER = forms.DecimalField(required=False)
    winnerPR = forms.DecimalField(required=False)
    loserER = forms.DecimalField(required=False)
    loserPR = forms.DecimalField(required=False)
    loserPR = forms.DecimalField(required=False)
    tags = forms.CharField(max_length=100,required=False)
    matfile  = forms.FileField(required=False)
    #matfile = forms.Field(widget=forms.FileInput(),required=False)
    #matfile = forms.FileInput(required=False)
    #enctype="multipart/form-data"



class User(Document):
    username = StringField(unique=True)
    firstname = StringField()
    lastname = StringField()
    rating = IntField()

class Match(Document):
        winner = ReferenceField(User)
        loser =  ReferenceField(User)
        winscore = IntField(required=True)
        losescore = IntField(required=True)
        matchlength = IntField(required=True)
        tags = ListField(StringField(max_length=30))
        date_modified = DateTimeField(default=datetime.datetime.now)
        matfile = StringField(max_length=30) #FileField()
        winnerER = DecimalField()
        winnerPR = DecimalField()
        loserER = DecimalField()
        loserPR = DecimalField()



def handle_uploaded_file(f, idf):
    destination = open('c:/tmp/'+idf + '.txt', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def doUser (n):
    usr = User.objects(username=n)
    if len(usr):
        usr = usr[0]
    else:
        usr = User(username=n)
    usr.save()
    return usr


