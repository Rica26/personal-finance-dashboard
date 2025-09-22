import { useState, useEffect, FormEvent } from "react";
import { createTransaction, getCategories } from "@/services";
import { Category } from "@/services/types";
import { parse } from "path";

type TransactionFormProps = {
  type: "income" | "expense";
  onSuccess: () => void;
};

export default function TransactionForm({ type, onSuccess }: TransactionFormProps) {
  const [amount, setAmount] = useState("");
  const [category, setCategory] = useState<number | "">("");
  const [date, setDate] = useState("");
  const [categories, setCategories] = useState<Category[]>([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    getCategories().then((res) => {
      const filtered = res.data.filter((cat) => cat.type === type);
      setCategories(filtered);
    });
  }, [type]);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!amount || !category || !date) return alert("Please fill all fields.");
    setLoading(true);
    try {
      await createTransaction({ amount: parseFloat(amount), category, date });
      setAmount("");
      setCategory("");
      setDate("");
      if (onSuccess) onSuccess();
    } catch (err) {
      console.error(err);
      alert("Error creating transaction.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="number" placeholder="Amount" value={amount} onChange={(e) => setAmount(e.target.value)} />
      <select value={category} onChange={(e) => setCategory(parseInt(e.target.value))}>
        <option value="">Select Category</option>
        {categories.map((cat) => (
          <option key={cat.id} value={cat.id}>
            {cat.name}
          </option>
        ))}
      </select>
      <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
      <button type="submit" disabled={loading}>{loading ? "Saving..." : "Add Transaction"}</button>
    </form>
  );
}
