from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'rating', 'comment']

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'reviews/restaurant_list.html', {'restaurants': restaurants})

def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    reviews = restaurant.reviews.all()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.save()
            return redirect('restaurant_detail', pk=restaurant.pk)
    else:
        form = ReviewForm()
        
    return render(request, 'reviews/restaurant_detail.html', {
        'restaurant': restaurant,
        'reviews': reviews,
        'form': form
    })
