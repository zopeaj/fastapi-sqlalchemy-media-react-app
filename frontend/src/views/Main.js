import { useState, Fragment, useEffect } from 'react';
import { Button, Grid, Skeleton, AppBar, Grid, Table, Breadcrumbs, Menu, FormControlLabel, MenuItem, TableBody, TableCell, TableHead, TableRow, Toolbar, Avatar, Divider, CircularProgress, LinearProgress, Radio, Modal, Container, Link, RadioGroup, Badge } from '@mui/material';
import { DesktopOutlined, PieChartOutlined, FileOutlined, TeamOutlined, UserOutlined, LoadingOutlined, Settings, Search,  PlusOutlined  } from "@mui/icons-material";
import CustomeDrawer from "../components/CustomerDrawer"
import { useGetCustomersQuery, useDeleteCustomerMutation } from '../data/user/api/customerApi';
import '../App.css';
import { errorNotification, successNotification } from '../components/Notification';



const TheAvatar = ({ name }) => {
  let trim = name.trim();
  if(trim.length === 0) {
    return <Avatar icon={<UserOutlined/>} />
  }

  return (
    <Avatar>
      {`${name.charAt(0)}`}
    </Avatar>
  );
}


const removeCustomer = (customerId) => {
  const { deleteCustomer, isLoading } = useDeleteCustomerMutation();
  try {
    deleteCustomer(customerId).unwrap();
    successNotification(open={open}, onClose={onClose}, message={message}, description={description})
  }catch(err) {
    console.error("Error trying to delete customer: ", err);
  }finally{
    errorNotification(open={open}, onClose={onClose}, message={message}, description={description})
  }
}

const columns = (customerId, open, onClose, message, description) => [
  {
    title: '',
    dataIndex: 'avatar',
    key: 'avatar',
    render: (text, customer) => <TheAvatar name={customer.name}/>
  },
  {
    title: 'id',
    dataIndex: 'id',
    key: 'id'
  },
  {
    title: 'Name',
    dataIndex: 'name',
    key: 'name',
  },
  {
    title: 'Email',
    dataIndex: 'email',
    key: 'email',
  },
  {
    title: 'Lastname',
    dataIndex: 'lastname',
    key: 'lastname'
  },
  {
    title: 'Age',
    dataIndex: 'age',
    key: 'age'
  },
  {
    title: 'Actions',
    key: 'actions',
    render: (text, customer) =>
      <RadioGroup>
        <Modal open={open} onClose={onClose} onConfirm={() => removeCustomer(customerId)}>
            <h3>{title `${customer.name}`}</h3>
            <p>{message}</p>
            <h4>{description}</h4>
            <Button onClick={onConfirm}>
              Delete
            </Button>
        </Modal>
        <Button onClick={() => alert("TODO: Implement edit customer")}>
          Edit
        </Button>
      </RadioGroup>
  }
]


const loadingProgress = <LinearProgress style={{ fontSize: 24 }} />


export const Main = () => {
  const { data, isLoading, isSuccess, isError, error, refetch, isFetching } = useGetCustomersQuery();
  const [openDrawer, setShowDrawer] = useState(false);
  const anchor = "right";

  const onCreate = () => {
    return null;
  };

  const onUpdate = () => {
    return null;
  };

  useEffect(() => {
    console.log("Component is mounted");
    refetch();
  }, []);


  const renderCustomers = () => {
    if(isFetching) {
      return (<CircularProgress color="secondary" />)
    }

    if(data.length <= 0) {
      return (
         <Fragment>
          <Button onClick={() => setShowDrawer(!openDrawer)} color="primary" variant="contained">
            <IconButton>
              <PlusOutlined />
            </IconButton>
            Add New Student
          </Button>
          <CustomeDrawer
            openDrawer={openDrawer}
            setShowDrawer={setShowDrawer}
            anchor={anchor}
          />
          <Skeleton animation="wave" />
         </Fragment>
      )
    }

    return (
      <Fragment>
        <CustomeDrawer
          openDrawer={openDrawer}
          setShowDrawer={setShowDrawer}
          anchor={anchor}
        />
        <Table>
         <TableHead>
           <TableRow>
             <TableCell>Avatar</TableCell>
             <TableCell>Name</TableCell>
             <TableCell>Email</TableCell>
             <TableCell>Lastname</TableCell>
             <TableCell>Age</TableCell>
           </TableRow>
         </TableHead>
         <TableBody>
           <TableContents data={customerId} open={open} onClose={onClose} message={message} description={description}/>
           <Badge count={data.length} className="site-badge-count"/>
           <Button onClick={() => setShowDrawer(!openDrawer)} variant="contained" color="primary">
             Add New Customer
           </Button>
         </TableBody>
        </Table>
      </Fragment>
    );
  }

  return (
    <Fragment>
      <Grid container>
        <Grid item>
          <Typography variant="title" component="div">
            Custom App
          </Typography>
          <Menu>
            <MenuItem>Profile</MenuItem>
            <MenuItem>Profile</MenuItem>
            <MenuItem>Profile</MenuItem>
          </Menu>
        </Grid>
        <Grid item>
          <AppBar>
            <Toolbar>
              <IconButton>
                <Settings />
              </IconButton>
              <IconButton>
                <Search />
              </IconButton>
            </Toolbar>
          </AppBar>
          <Container maxWidth="sm">
            <Breadcrumbs style={{margin: '16px 0' }}>
              <Link underline="hover" color="inherit" href="#">
                  User
              </Link>
              <Link underline="hover" color="inherit" href="#">
                  Bill
              </Link>
            </Breadcrumbs>
            <div class="site-layout-background" style={{ padding: 24, minHeight: 360 }}>
              {renderCustomers()}
            </div>
          </Container>
          <div style={{ textAlign: 'center' }}>
            <Avatar src="" />
          </div>
          <Divider>
            <a rel="noopener noreferer" target="_blank"
            href="https://zopeaj.com">
              Click here to access Fullstack FastAPI & React for proefessionals
            </a>
          </Divider>
        </Grid>
     </Grid>
    </Fragment>
  );
}

export default Main;
