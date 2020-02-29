import React, { Component } from 'react';
// import storage from "../Firebase/index";
// import {Grid} from '@material-ui/core';
// import {Searchbar,VideoDetail} from './components'
import FileUploader from 'react-firebase-file-uploader';
import firebase from 'firebase';
import config from './firebase-config';

firebase.initializeApp(config);

class Watch extends Component{
  // handleSubmit = async (searchTerm) => {
  //   const resonse = await
  // }
  /*render() {
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
  }*/

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
    firebase.storage().ref('eye_vids').child(filename).getDownloadURL()
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

    console.log(this.state)
    return (
      <div>

        <label> Progress:</label>
          <p>{this.state.progress}</p>
          <br/>
          <br/>
          <br/>

          <label> Video:</label>
          {this.state.video && <vid src={this.state.videoURL}/>}

          <hr/>
          {this.state.videoURL && <a href={this.state.videoURL}>Download</a>}
        <br/>
        <br/>
        <br/>


        <FileUploader
          accept="video/*"
          name='video'
          storageRef={firebase.storage().ref('eye_vids')}
          onUploadStart={this.handleUploadStart}
          onUploadSuccess={this.handleUploadSuccess}
          onProgress={this.handleProgress}
        />

      </div>
    );
  }
}
export default Watch;
