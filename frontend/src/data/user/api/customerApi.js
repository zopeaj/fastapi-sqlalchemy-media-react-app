import { fetchBaseQuery, createApi } from '@reduxjs/toolkit/query/react';
import { initialState } from '../customer.state';
import { customersAdapter } from '../customer.state'

export const customerApi = createApi({
  reducerPath: 'customerApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://localhost:9091/api/v1/' }),
  tagTypes: ['Customer'],
  endpoints: (builder) => ({
    getCustomerById: builder.query({
      query: (customerId) => `customer/${customerId}`,
      providesTags: (result, error, arg) => result ? [{type: 'Customer', result}] : error?.status === 404 ? ['CUSTOMER_NOT_FOUND'] : ['UNKNOWN_ERROR'],
    }),
    getCustomers: builder.query({
      query: () => 'customer',
      providesTags: (result = [], error, arg) = [
        'Customer',
        ...result.map(({ id }) => ({ type: 'Customer', id }))
      ],
      transformResponse: responseData => {
        return customersAdapter.setAll(initialState, responseData)
      },
      invalidatesTags: ['Customer']
    }),
    createNewCustomer: builder.mutation({
      query: initialPost => ({
        url: 'customer',
        method: 'POST',
        body: JSON.stringify(initialPost),
        headers: {
          "Content-Type": "application/json"
        }
      }),
    }),
    editCustomer: builder.mutation({
      query: (data, id) => ({
        url: `customer/${id}`,
        method: 'PUT',
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json",
        }
      }),
      invalidatesTags: (result, error, arg) => [{type: 'Customer', id: arg.id}]
    }),
    deleteCustomer: builder.mutation({
      query: (id) => ({
        url: `customer/${id}`,
        method: 'DELETE',
      })
    })
  }),
});


export const createCustomer = async (data) => {
  var formData = new FormData();
  formData.append("name", data.name);
  formData.append("email", data.email);
  formData.append("age", data.age);
  formData.append("userimage", data.files);

  var requestOptions = {
    method: 'POST',
    body: formData,
  }

  const customerData = {}

  await fetch("http://localhost:8082/api/v1/customer", requestOptions)
  .then(response => response.text())
  .then(result => {
    customerData["result"] = result;
  })
  .catch(error => {
    customerData["error"] = error;
  });

  return customerData
}

export const getAllCustomer = async () => {
  const customerData = {};
  await fetch("http://localhost:8081/api/v1/customer", {
    method: "GET",
    headers: {
      ContentType: "application/json"
    }
  }).then(response => response.text())
    .then(result => {
      customerData["result"] = result;
    })
    .catch(error => {
      customerData["error"] = error;
    });

    return customerData;
}

export const updateCustomer = async (data, id) => {
  const customerData = {};
  await fetch(`http://localhost:8081/api/v1/customer/${id}`, {
    method: "PUT",
    body: JSON.stringify(data),
    headers: {
      ContentType: "application/json"
    }
  }).then(response => response.text())
  .then(result => {
    customerData["result"] = result;
  })
  .then(error => {
    customerData["error"] = error;
  });
  return customerData;
}

export const deleteCustomer = async (id) => {
  const customerData = {};
  await fetch(`http://localhost:8081/api/v1/customer/${id}`, {
    method: "DELETE",
  }).then(response => response.text())
  .then(result => {
    customerData["result"] = result;
  })
  .then(error => {
    customerData["error"] = error;
  });
  return customerData;
}

export const { useGetCustomerById, useGetCustomers, useCreateCustomerMutation, useUpdateCustomerMutation, useDeleteCustomerMutation} = customerApi;
