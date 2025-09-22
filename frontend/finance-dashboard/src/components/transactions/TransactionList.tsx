"use-client";
import React, { useEffect, useState } from "react";
import { getIncomeTransactions, getExpenseTransactions } from "@/services";

import { Transaction } from "@/services/types";
import TransactionItem from "./TransactionItem";

type TransactionListProps = {
  type: "income" | "expense";
};

export default function TransactionList({ type }: TransactionListProps) {
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    const fetchTransactions = type === "income" ? getIncomeTransactions : getExpenseTransactions;
    fetchTransactions()
      .then((res) => setTransactions(res.data))
      .finally(() => setLoading(false));
  }, [type]);

  if (loading) return <p>Loading...</p>;
  if (transactions.length === 0) return <p>No transactions found.</p>;

  return (
    <ul>
      {transactions.map((tx) => (
        <TransactionItem key={tx.id} transaction={tx} />
      ))}
    </ul>
  );
}
