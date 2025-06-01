from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum

def list_expenses(request):
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'expenses/list.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses:list_expenses')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add.html', {'form': form})

def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    form = ExpenseForm(request.POST or None, instance=expense)
    if form.is_valid():
        form.save()
        return redirect('expenses:list_expenses')
    # Pass the expense object to the template for pre-filling fields
    return render(request, 'expenses/edit.html', {'form': form, 'expense': expense})

def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect('expenses:list_expenses')

def summary(request):
    total = Expense.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    # For bar chart: each expense
    expenses = Expense.objects.all().order_by('-date')
    expense_titles = [e.title for e in expenses]
    expense_amounts = [float(e.amount) for e in expenses]
    # Group by category for chart
    category_data = (
        Expense.objects.values('category')
        .order_by('category')
        .annotate(total=Sum('amount'))
    )
    # Prepare data for chart.js
    categories = [item['category'] for item in category_data]
    amounts = [float(item['total']) for item in category_data]
    return render(request, 'expenses/summary.html', {
        'total': total,
        'expenses': expenses,
        'expense_titles': expense_titles,
        'expense_amounts': expense_amounts,
        'categories': categories,
        'amounts': amounts,
    })