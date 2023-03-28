import { Snackbar, Fade, Grow, IconButton, Slide } from "@mui/material";
import { CloseIcon } from "@mui/icons-material";


const SuperNotification = ({ transition, direction, top, right, onClose, message, ...rest}) => {
  return (
    <Snackbar
      TransitionComponent={{ slide: Slide, grow: Grow, fade: Fade }[transition]}
      TransitionProps={{ direction }}
      anchorOrigin={{
        vertical: {top},
        horizontal: {right}
      }}
      message={message}
      action={[
         <IconButton color="inherit"
           onClick={onClose}>
           <CloseIcon />
         </IconButton>
      ]}
      {...rest}
    />
  );
};


export const successNotification = (open, onClose, message, description) => {
  return (
     <SuperNotification open={open} onClose={onClose} autoHideDuration={5000} message={message} top="top" right="right" transition="slide" direction="up" />
  )
}

export const errorNotification = (open, onClose, message, description) => {
  return (
    <SuperNotification open={open} onClose={onClose} autoHideDuration={5000} message={message} top="top" right="right" transition="slide" direction="up" />
  );
}

export const infoNotification = (open, onClose, message, description) => {
  return (
    <SuperNotification open={open} onClose={onClose} autoHideDuration={5000} message={message} top="top" right="right" transition="slide" direction="up" />
  );
}

export const warningNotification = (open, onClose, message, description) => {
  return (
    <SuperNotification open={open} onClose={onClose} autoHideDuration={5000} message={message} top="top" right="right" transition="slide" direction="up" />
  );
}
