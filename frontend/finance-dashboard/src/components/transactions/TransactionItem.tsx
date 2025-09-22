import { Transaction } from "@/services";

type TransactionItemProps = {
  transaction: Transaction;
};

export default function TransactionItem({ transaction }: TransactionItemProps) {
  return (
    <li>
      {transaction.category_name} - ${transaction.amount} - {transaction.date}
    </li>
  );
}