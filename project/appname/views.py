from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import Category, Budget, Expense
from .forms import CategoryForm,SignupForm,BudgetForm

# Create your views here.
@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    context= {
        "categories": categories,
    }

    return render(request,'appname/index.html',context)

@login_required
def expense_create(request,id):
    

    return render(request,'appname/expense-create.html')

@login_required
def budget_create(request,id):
    c = Category.objects.get(id=id)
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.category = c
            x.user = request.user
            x.save()
            return redirect('category_list')
    else:
        form = BudgetForm()
    return render(request, 'appname/budget-create.html', {'form': form})
    
    # return render(request,'appname/budget-create.html')

# @login_required
# def add_category(request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = CategoryForm()
#     return render(request, 'appname/add_category.html', {'form': form})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.user = request.user
            x.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'appname/add_category.html', {'form': form})

@login_required
def update_category(request,pk):
    single_cat = Category.objects.get(id=pk)
    form = CategoryForm(instance=single_cat)

    if request.method== 'POST':
        form = CategoryForm(request.POST, instance=single_cat)
        if form.is_valid():
            x = form.save(commit=False)
            x.user = request.user
            x.save()
            return redirect('category_list')
    context={'form': form}
    return render(request, 'appname/add_category.html', context )

@login_required
def delete_category(request,pk):
    single_cat= Category.objects.get(id=pk)
    single_cat.delete()
    return redirect('category_list')

def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = SignupForm()
    context={
        'form': form
    }
    return render(request,'appname/signup.html',context)

def signout(request):
    logout(request)
    return redirect('login')

@login_required
def budget_view(request,pk):
    cate = Category.objects.get(id=pk)
    budget = Budget.objects.filter(category=cate)
    print(budget)
    context ={
        "budget": budget,
    }
    return render(request,'appname/budget_view.html',context)
