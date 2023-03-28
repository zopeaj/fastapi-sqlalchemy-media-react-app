import { createEntityAdapter } from '@reduxjs/toolkit';

export const initialState = createEntityAdapter.getInitialState({
  "customers": [],
  name: '',
  email: '',
  lastname: '',
  age: '',
});

export const customersAdapter =createEntityAdapter();
