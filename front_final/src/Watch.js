import React from 'react';
import {Grid} from '@material-ui/core';
import {Searchbar,VideoDetail} from './components'
import video from './assets/demo_test.mp4'
import image from './assets/pie_chart.jpg'
import image1 from './assets/graph.jpg'
class Watch extends React.Component{
  // handleSubmit = async (searchTerm) => {
  //   const resonse = await
  // }
  render() {
    return(
    <Grid justify="center" container spacing={10}>
      <Grid item xs={12}>
        <Grid container spacing ={10}>
          <Grid item xs={12}>
            <Searchbar onFormSubmit={this.handleSubmit}/>
            <div className = "Watch" >
              <h1>This is your result</h1>
              <video width="1050" height="500" controls >
              <source src={video} type="video/mp4"/>
              </video>
              </div>
            <Grid
              container
              direction="row"
              justify="space-around"
              alignItems="center"
            >
              <Grid item xs={6}>
                <img src={image} width="505" height="300" />
                </Grid>
              <Grid item xs={6}>
              <img src={image1} width="505" height="300" />
                </Grid>
            </Grid>
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
