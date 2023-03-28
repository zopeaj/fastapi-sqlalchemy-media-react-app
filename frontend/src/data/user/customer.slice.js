import { createSlice } from "@reduxjs/toolkit";
import { initialState } from './customer.state';
import { actionCustomerCreate, actionCustomerUpdate, actionGetAllCustomers, actionCustomerDelete } from "./customer.actions";


export const customerSlice = createSlice({
  name: 'customer',
  initialState,
  reducers: {

  },
  extraReducers: (builder) => {
    builder
      .addCase(actionCustomerCreate.pending, (state, action) => {

      })
      .addCase(actionCustomerCreate.fulfilled, (state, action) => {

      })
      .addCase(actionCustomerCreate.rejected, (state, action) => {

      });
  }
});

export default customerSlice.reducer;
