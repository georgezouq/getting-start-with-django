from django.shortcuts import render, redirect
from .models import TodoItem
from redis import Redis

redis = Redis(host='redis', port=6379)

def index(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = TodoItem.objects.all()
    counter = redis.incr('counter')
    return render(request, 'index.html', {'item': items, 'counter': counter})
