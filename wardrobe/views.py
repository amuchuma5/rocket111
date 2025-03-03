from django.shortcuts import render, redirect, get_object_or_404
from .models import ClothingItem
from .forms import ClothingItemForm

# Create your views here.
def clothing_list(request):
    items =ClothingItem.objects.all()
    return render(request,'clothing_list.html',{'items':items})
def clothing_create(request):
    if request.method == "POST":
        form =ClothingItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(clothing_list)
        else:
            form =ClothingItemForm
            return render(request,'clothing_form.html',{'form':form})
def clothing_update(request,pk):
    item = get_object_or_404(ClothingItem, pk=pk)
    if request.method == "POST":
        form = ClothingItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(clothing_list)
        else:
            form = ClothingItemForm(instance=item)
            return render(request,'clothing_form.html',{'form':form})

def clothing_delete(request,):
    item =get_object_or_404(ClothingItem)
    if request.method == "POST":
        item.delete()
        return redirect(clothing_list)
    return render(request,'clothing_confirm_delete.html',{'item':item})


