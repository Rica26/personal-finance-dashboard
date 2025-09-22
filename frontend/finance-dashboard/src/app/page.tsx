"use client";

import Image from "next/image";
import { useEffect, useState } from "react";
import { getTransactions } from "../services/api";
import styles from "./page.module.css";

export default function Home() {
const [transactions, setTransactions] = useState<any[]>([]);

  useEffect(() => {
    getTransactions()
      .then(res => setTransactions(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <ul>
      {transactions.map((t) => (
        <li key={t.id}>{`Transaction ${t.id}: ${t.amount}`}</li>
      ))}
    </ul>
  );
}
