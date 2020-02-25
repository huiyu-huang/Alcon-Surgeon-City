import React from 'react';
import {Paper, TextField} from '@material-ui/core';


class Searchbar extends React.Component {
  state={
    searchTerm: '',
  }

  handleChange = (event) => this.setState({searchTerm: event.target.value});

  // handleSubmit = (event) => {
  //   const{searchTerm} = this.state;
  //   const{onFormSubmit} = this.props;
  //   onFormSubmit(searchTerm);
  //   event.preventDefault();
  // }
  render () {
    return(
      <Paper elevation={6} stlye={{padding: '25px'}}>
        <form onSubmit={this.handelSubmit}>
          <TextField fullWidth label="Search ..." onChange={this.handleChange}/>
        </form>
      </Paper>
    );
  }
  // render(){
  //   return(
  //     <h1>this is a searchBar</h1>
  //   )
  // }
 }
export default Searchbar
