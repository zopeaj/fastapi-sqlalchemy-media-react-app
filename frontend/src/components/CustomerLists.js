import { useEffect } from "react";
import {
    Skeleton,
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableRow,
    CircularProgress,
    Divider,
    Paper,
    Spinner,
    Modal,
    Avatar
 } from "@mui/material";
import { useGetCustomers } from "../data/user/api/customerApi";
import { Person } from "@mui/icons-material";
import { useCustomerListStyles } from "../styles/customerListStyles";




export const CustomerList = () => {
  const { data: customers, isLoading, isSuccess, isError, error, refetch, isFetching } = useGetCustomers();
  const classes = useCustomerListStyles();
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(false);

  const onOpen = () => {
    setOpen(!open);
  }

  const onClose = () => {
    setOpen(false);
  }

  let content;

  if (isLoading) {
     content = (<Spinner text="Loading..." />)
  } else if(isSuccess) {
    content = customers.map(customer => (
      <PostListData key={customer.id} post={customer} />
    ));
  } else if(isError) {
    content =  (<div>{error.toString()}</div>)
  }

  const LoadingContainer = ({ loading }) => {
    return loading ? (<CircularProgress className={classes.progress}  />) : null;
  }

  const onDelete = (id) => {

  };

  const onUpdate = (id) => {

  }


  return (
     <div className="customer-container">
       <Table>
         <TableHead>
           <TableRow>
             <TableCell>...</TableCell>
             <TableCell>Id</TableCell>
             <TableCell>Name</TableCell>
             <TableCell>Email</TableCell>
             <TableCell>LastName</TableCell>
           </TableRow>
         </TableHead>
         <TableBody>
           {customers.map((cutomer, index) => (
             <TableRow key={customer.id}>
               <TableCell component="th" scope="row">
                 <Avatar>
                   <Person />
                 </Avatar>
               </TableCell>
               <TableCell>
                 {customer.id}
               </TableCell>
               <TableCell>
                 {customer.name}
               </TableCell>
               <TableCell>
                 {customer.email}
               </TableCell>
               <TableCell>
                 {customer.lastname}
               </TableCell>
               <TableCell>
                 <Button color="primary" variant="contained" onClick={() => onDelete(`${customer.id}`)}>
                   Delete
                 </Button>
                 <Button color="secondary" variant="contained" onClick={() => onUpdate(`${customer.id}`)}>
                   Delete
                 </Button>
               </TableCell
             </TableRow>
           ))}
         </TableBody>
       </Table>
       <LoadingContainer loading={isLoading} />
     </div>
  );
}

