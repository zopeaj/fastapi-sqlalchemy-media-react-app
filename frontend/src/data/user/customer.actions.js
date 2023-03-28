import { createAsyncThunk } from '@reduxjs/toolkit';
import { createCustomer, updateCustomer, getAllCustomer, deleteCustomer } from "./api/userApi";

const actionCustomerCreate = createAsyncThunk("customer/create", async (data) => {
  const response = await createCustomer(data);
  return response;
});

export const actionCustomerUpdate = createAsyncThunk("customer/update", async (data, id) => {
  const response = await updateCustomer(data, id);
  return response;
});

export const actionGetAllCustomers = createAsyncThunk("customer/all", async () => {
  const response = await getAllCustomer();
  return response;
});

export const actionCustomerDelete = createAsyncThunk("customer/delete", async (id) => {
  const response = await deleteCustomer(id);
  return response;
});



