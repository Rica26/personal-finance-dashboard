export type Category = {
    id: number;
    name: string;
    type: 'income' | 'expense';
}

export type Transaction = {
  id: number;
  amount: number;
  category: number;
  category_name: string;
  category_type?: 'income' | 'expense';
  date: string;
  created_at: string;
  updated_at: string;
};

// Para endpoints de resumo mensal/anual
export type YearlyTotal = {
  year: number;
  total: number;
}

export type MonthlyTotal = {
  year: number;
  month: number;
  total: number;
}

// Para endpoints que agrupam por categoria
export type CategoryTotal = {
  category__name: string;
  total: number;
}

// Para endpoints que agrupam por mês e categoria
export type MonthlyCategoryTotal = {
  month: number;
  category__name: string;
  total: number;
}