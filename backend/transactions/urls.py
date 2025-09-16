from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ExpenseAPIView, IncomeAPIView, TransactionViewSet, CategoryViewSet, IncomeYearlyAPIView, IncomeYearlyTotalAPIView, IncomeYearlyCategoryAPIView, IncomeYearlyMonthlyCategoryAPIView, IncomeMonthlyAPIView, IncomeMonthlyCategoryAPIView, ExpenseYearlyAPIView, ExpenseYearlyTotalAPIView, ExpenseYearlyCategoryAPIView, ExpenseYearlyMonthlyCategoryAPIView, ExpenseMonthlyAPIView, ExpenseMonthlyCategoryAPIView

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('transactions/income/', IncomeAPIView.as_view(), name='income'),
    path('transactions/income/yearly/<int:year>/', IncomeYearlyAPIView.as_view(), name='income-yearly'),
    path('transactions/income/yearly/<int:year>/total/', IncomeYearlyTotalAPIView.as_view(), name='income-yearly-total'),
    path('transactions/income/yearly/<int:year>/category/', IncomeYearlyCategoryAPIView.as_view(), name='income-yearly-category'),
    path('transactions/income/yearly/<int:year>/monthly-category/', IncomeYearlyMonthlyCategoryAPIView.as_view(), name='income-yearly-monthly-category'),
    path('transactions/income/monthly/<int:year>/<int:month>/', IncomeMonthlyAPIView.as_view(), name='income-monthly'),
    path('transactions/income/monthly/<int:year>/<int:month>/category/', IncomeMonthlyCategoryAPIView.as_view(), name='income-monthly-category'),
    path('transactions/expense/', ExpenseAPIView.as_view(), name='expense'),
    path('transactions/expense/yearly/<int:year>/', ExpenseYearlyAPIView.as_view(), name='expense-yearly'),
    path('transactions/expense/yearly/<int:year>/total/', ExpenseYearlyTotalAPIView.as_view(), name='expense-yearly-total'),
    path('transactions/expense/yearly/<int:year>/category/', ExpenseYearlyCategoryAPIView.as_view(), name='expense-yearly-category'),
    path('transactions/expense/yearly/<int:year>/monthly-category/', ExpenseYearlyMonthlyCategoryAPIView.as_view(), name='expense-yearly-monthly-category'),
    path('transactions/expense/monthly/<int:year>/<int:month>/', ExpenseMonthlyAPIView.as_view(), name='expense-monthly'),
    path('transactions/expense/monthly/<int:year>/<int:month>/category/', ExpenseMonthlyCategoryAPIView.as_view(), name='expense-monthly-category'),
]

urlpatterns += router.urls
