"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def project1(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/project1.html',
        {
            'title':'VOC en WIC',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'benmat':'Benodigd materiaal',          
            'algleer':'Algemene leerdoelen',            
            'pdf':'Link to PDF article',        


        }
    )

def project2(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/project2.html',
        {
            'title':'Latijn: vroeger en nu',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'benmat':'Benodigd materiaal',          
            'algleer':'Algemene leerdoelen',   
            'pdf':'Link to PDF article',        

        }
    )