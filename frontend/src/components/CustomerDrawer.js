import { useState, Fragment } from '@react';
import { Drawer, Grid, TextInput, MenuItem, Select, InputLabel, Grid, Button, Box, LinearProgress, Snackbar } from '@mui/material';
import { useCreateCustomerMutation } from "../data/user/api/customerApi";
import { errorNotification, successNotification } from "./Notification";


export const CustomerDrawer = ({openDrawer, setShowDrawer, anchor}) => {
  const [ createNewCustomer ] = useCreateCustomerMutation();
  const onClose = () => setShowDrawer(false);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [lastname, setLastName] = useState('');
  const [age, setAge] = useState('');
  const [openNotification, setOpenNotification] = useState(true);
  const [submitting, setSubmitting] = useState(false);

  const canSave = [ name, email, lastname, age ].every(Boolean) && !isLoading

  const onSaveCustomer = async () => {
    if(canSave) {
      try {
        setSubmitting(true);
        await createNewCustomer({ name, email, lastname, age }).unwrap()
        successNotification(openNotification, setOpenNotification, "Customer Successfully added", `${name} was added to the system`);
        setName('')
        setEmail('')
        setLastName('')
        setAge('')
      }catch(err) {
        console.error('Failed to see the post: ', err);
        errorNotification(openNotification, setOpenNotification, `${err.message} [${res.status}] [${err.error}]`);
      }finally {
        setSubmitting(false);
      }
    }
  }


  return (
    <Fragment>
      <Drawer anchor={anchor} open={openDrawer} onClose={onClose}>
            <section>
              <h2>Add a New Customer</h2>
              <form onSubmit={onSaveCustomer}>

                <Grid container>
                  <Grid item>
                    <label htmlFor="customerName">Name: </label>
                    <input type="text" id="name" name="name" placeholder="Please enter customer name" onChange={onNameChange} required/>
                  <Grid item>
                  <Grid item>
                    <label htmlFor="customerEmail">Email: </label>
                    <input type="text" id="email" name="name" placeholder="Please enter customer Email" onChange={onEmailChange} required/>
                  </Grid>
                  <Grid item>
                    <label htmlFor="customerLastname">Lastname: </label>
                    <input type="text" id="lastname" name="name" placeholder="Please enter customer Lastname" onChange={onLastNameChange} required/>
                  </Grid>

                  <Grid item>
                    <InputLabel id="demo-simple-select-label">Age</InputLabel>
                    <Select labelId="demo-simple-select-label" value={age} label="Age" onChange={handleAgeChange} required>
                       <MenuItem value={10}>Ten</MenuItem>
                       <MenuItem value={20}>Twenty</MenuItem>
                       <MenuItem value={30}>Thirty</MenuItem>
                    </Select>
                  </Grid>

                  <Grid item>
                    <Box component="span" sx={{ p: 2, border: '1px dashed grey' }}>
                        <Button htmlType="submit">Submit</Button>
                    </Box>
                  </Grid>

                  <Grid item>
                    {submitting && <LinearProgress color="secondary" />}
                  </Grid>
                </Grid>
              </form>
            </section>
            <div style={{ textAlign: 'right' }}>
              <Button variant="submit" onClick={onClose} style={{ marginRight: 8 }}>
                Cancel
              </Button>
            </div>
      </Drawer>
    </Fragment>
  );
}
