import React from 'react';
import {Grid} from '@material-ui/core';
import {Searchbar,VideoDetail} from './components'
import video from './assets/demo_test.mp4'
import image from './assets/pie_chart.jpg'
import image1 from './assets/graph.jpg'
import app from './components/Firebase/base'
import classAtt from './ClassAtt'
import axios from "axios";

class Watch extends React.Component{
  // handleSubmit = async (searchTerm) => {
  //   const resonse = await
  // }
  state = {
     a: [],
     got:false
  };
  componentDidMount() {
     this.getUsers();
  }
  getUsers = async () => {
      let res = await axios.get("/watch");
      let stuff  = res.data;
      console.log("hi", stuff)
      console.log("we are here")
      this.setState({got:true})
      console.log(this.state.got)
      this.setState({a:stuff.info})
      console.log(this.state.a)
      console.log("now here")
  };


  render() {
    return(
      <div>
          {this.state.got === false ? (
              <div>Loading...</div>
          ) :
          <div>
          <Grid item xs={12}>
            <h2>This is your result</h2>
            <Grid
              container
              direction="row"
              justify="flex-start"
              alignItems="center"
            >
              <Grid item xs={8}>
                <video width="800" height="550" controls >
                  <source src={video} type="video/mp4"/>
                </video>
              </Grid>
              <Grid item xs={3}>
                <Grid
                  container
                  direction="column"
                  justify="center"
                  alignItems="flex-end"
                  >
                    <Grid item xs={6}>
                      <img src={image} alt="" width="400" height="275" />
                    </Grid>
                    <Grid item xs={6}>
                    <img src={image1} alt="" width="400" height="275" />
                    </Grid>
                </Grid>
              </Grid>

            </Grid>
          </Grid>

          <Grid item xs={8}>
            <VideoDetail />
          </Grid>
          <Grid item xs={4}>
          </Grid>
      </div>
    }
    </div>
  )
  }
}
export default Watch;
