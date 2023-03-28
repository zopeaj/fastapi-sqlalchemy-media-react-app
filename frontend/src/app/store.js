import { configureStore } from '@reduxjs/toolkit';
import customerReducer from '../data/user/user.slice';

export const store = configureStore({
  reducer: {
    customer: customerReducer,
  },
});
