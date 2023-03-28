import { useSelector } from "@reduxjs/toolkit";

const getAllCustomer = (state) => state.customers;
export const readAllCustomer = useSelector(getAllCustomer);

