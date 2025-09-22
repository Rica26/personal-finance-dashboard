import axios from "axios";
import { Category, Transaction, YearlyTotal, MonthlyTotal, MonthlyCategoryTotal, CategoryTotal } from "./types";

const api = axios.create({
  baseURL: "http://localhost:8000/",
});

// ----------------- TRANSACTIONS -----------------

//CRUD
export const createTransaction = (data: Partial<Transaction>) => api.post<Transaction>("/transactions/", data);
export const updateTransaction = (id: number, data: Partial<Transaction>) =>
  api.put<Transaction>(`/transactions/${id}/`, data);
export const deleteTransaction = (id: number) => api.delete(`/transactions/${id}/`);

// Income Endpoints
export const getIncomeTransactions = () => api.get<Transaction[]>("/transactions/income/");
export const getIncomeYearly = (year: number) => api.get<MonthlyTotal[]>(`/transactions/income/yearly/${year}/`);
export const getIncomeYearlyTotal = (year: number) => api.get<YearlyTotal>(`/transactions/income/yearly/${year}/total/`);
export const getIncomeYearlyByCategory = (year: number) =>
  api.get<CategoryTotal[]>(`/transactions/income/yearly/${year}/category/`);
export const getIncomeYearlyMonthlyCategory = (year: number) =>
  api.get<MonthlyCategoryTotal[]>(`/transactions/income/yearly/${year}/monthly-category/`);
export const getIncomeMonthly = (year: number, month: number) =>
  api.get<MonthlyTotal>(`/transactions/income/monthly/${year}/${month}/`);
export const getIncomeMonthlyCategory = (year: number, month: number) =>
  api.get<CategoryTotal[]>(`/transactions/income/monthly/${year}/${month}/category/`);

// Expense Endpoints
export const getExpenseTransactions = () => api.get<Transaction[]>("/transactions/expense/");
export const getExpenseYearly = (year: number) => api.get<MonthlyTotal[]>(`/transactions/expense/yearly/${year}/`);
export const getExpenseYearlyTotal = (year: number) => api.get<YearlyTotal>(`/transactions/expense/yearly/${year}/total/`);
export const getExpenseYearlyByCategory = (year: number) =>
  api.get<CategoryTotal[]>(`/transactions/expense/yearly/${year}/category/`);
export const getExpenseYearlyMonthlyCategory = (year: number) =>
  api.get<MonthlyCategoryTotal[]>(`/transactions/expense/yearly/${year}/monthly-category/`);
export const getExpenseMonthly = (year: number, month: number) =>
  api.get<MonthlyTotal>(`/transactions/expense/monthly/${year}/${month}/`);
export const getExpenseMonthlyCategory = (year: number, month: number) =>
  api.get<CategoryTotal[]>(`/transactions/expense/monthly/${year}/${month}/category/`);

// ----------------- CATEGORIES -----------------

export const getCategories = () => api.get<Category[]>("/categories/");
export const getCategory = (id: number) => api.get<Category>(`/categories/${id}/`);
