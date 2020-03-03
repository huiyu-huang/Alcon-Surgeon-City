import React from 'react';
import {Grid} from '@material-ui/core';
import {Searchbar,VideoDetail} from './components'
import video from './assets/demo_test.mp4'
import image from './assets/pie_chart.jpg'
import image1 from './assets/graph.jpg'
import app from './components/Firebase/base'

class Watch extends React.Component{
  // handleSubmit = async (searchTerm) => {
  //   const resonse = await
  // }
  state = {
    video: '',
    videoURL: '',
    progress: 0
  }

  handleUploadStart = () => {
    this.setState({
      progress: 0
    })
  }

  handleUploadSuccess = filename => {
    this.setState({
      video: filename,
      progress: 100
    })
    app.storage().ref('eye_vids').child(filename).getDownloadURL()
      .then(url => this.setState({
        videoURL: url
      }))
  }

  handleProgress = progress => {
    this.setState({
      progress: progress
    })
  }


  render() {
    return(
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

  )
  }
}
export default Watch;
