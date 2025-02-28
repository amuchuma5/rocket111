from django.shortcuts import render, redirect, get_object_or_404
from .models import ClothingItem
from .forms import ClothingItemForm

# Create your views here.
def clothing_list(request):
    items =ClothingItem.objects.all()
    return render(request,'wardrobe/clothing_list.html',{'items':items})
def clothing_create(request):
    if request.method == "POST":
        form =ClothingItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(clothing_list)
        else:
            form =ClothingItemForm
            return render(request,'wardrobe/clothing_create.html',{'form':form})
def clothing_delete(request,pk):
    item =get_object_or_404(ClothingItem)
    if request.method == "POST":
        item.delete()
        return redirect(clothing_list)
    return render(request,'wardrobe/clothing_delete.html',{'item':item})

