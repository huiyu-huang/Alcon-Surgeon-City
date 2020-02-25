import React from 'react';
import {Grid} from '@material-ui/core';
import {Searchbar,VideoDetail} from './components'


class Watch extends React.Component{
  // handleSubmit = async (searchTerm) => {
  //   const resonse = await
  // }
  render() {
    return(
    <Grid justify="center" container spacing={16}>
      <Grid item xs={12}>
        <Grid container spacing ={16}>
          <Grid item xs={12}>
            <Searchbar onFormSubmit={this.handleSubmit}/>
          </Grid>
          <Grid item xs={8}>
            <VideoDetail />
          </Grid>
          <Grid item xs={4}>

          </Grid>
        </Grid>
      </Grid>
    </Grid>
  )
  }
}
export default Watch;
