from django.shortcuts import render, redirect
from .models import Review
from django.db.models import Avg

# Other static views
def ex(request):
    return render(request, 'ex.html')

def pone(request):
    return render(request, 'pone.html')

def ptwo(request):
    return render(request, 'ptwo.html')

def pthree(request):
    return render(request, 'pthree.html')

def pfour(request):
    return render(request, 'pfour.html')

# Review submission and display
def review_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = int(request.POST.get('rating'))
        comment = request.POST.get('comment')

        Review.objects.create(
            name=name,
            email=email,
            rating=rating,
            comment=comment
        )
        return redirect('review_page')  # Redirect to avoid form resubmission

    reviews = Review.objects.all().order_by('-created_at')

    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    return render(request, 'review.html', {
        'reviews': reviews,
        'average_rating': round(avg_rating, 1),
    })
