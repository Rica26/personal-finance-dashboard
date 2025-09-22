import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000/',
})

export const getTransactions = () => api.get("/transactions/");
export const createTransaction = (data: any) => api.post("/transactions/", data);