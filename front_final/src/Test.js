import React, {Component} from 'react';
import './App.css';
import axios from 'axios';

class Test extends React.Component {
  state={
    selectedFile:null
  }
  fileSelectedHandler=event=>{
    this.setState({
      selectedFile:event.target.files[0]
    })
  }
  fileUploadHandler = () => {
    const fd = new FormData();
    fd.append('video', this.state.selectedFile, this.state.selectedFile.name)
    axios.post(' /upload', fd, {
      onUploadProgress: progressEvent => {
        console.log('Upload Progress: ' + Math.round(progressEvent.loaded / progressEvent.total*100) + '%')
    }
     })
    .then(res=>{
      console.log(res);
    });
  }
  render(){
    return(
      <div onSubmit={this.onFormSubmit}>
        <h2>This is a test upload section</h2>
          <input type ="file" name="file" onChange={this.fileSelectedHandler}/>
          <button onClick={this.fileUploadHandler}>Upload</button>
      </div>
    );
  }
}
export default Test;
