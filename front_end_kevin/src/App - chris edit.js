import React, {Component} from 'react'
import useFileHandlers from './useFileHandlers'
import ReactDOM from 'react-dom';

import './App.css'

const Input = (props) => (
  <input
    type="file"
    accept="video/*"
    name="img-loader-input"
    multiple
    {...props}
  />
)

const App = () => {
  const {
    files,
    pending,
    next,
    uploading,
    uploaded,
    status,
    onSubmit,
    onChange,
  } = useFileHandlers()

  
class Form1 extends Component{
    render(){
        return (
            <div class="form">

                <form action="http://localhost:5000/handleUpload" method="post" enctype="multipart/form-data" id="root">
                  <input type="file" name="photo" class="button"/>{"\n"}
                  <input type="submit" value="Upload" class="button"/>
                </form>
            </div>
        );
    }
}


ReactDOM.render(
    <Form1/>,
    document.getElementById('root')
);

  return (
    <div className="container">
      <form className="form" onSubmit={onSubmit}>
        {status === 'FILES_UPLOADED' && (
          <div className="success-container">
            <div>
              <h2>Congratulations!</h2>
              <small>You uploaded your files. Get some rest.</small>
            </div>
          </div>
        )}
        <div>
          <Input onChange={onChange} />
          <button type="submit">Submit</button>
        </div>
        <div>
          {files.map(({ file, src, id }, index) => (
            <div
              style={{
                opacity: uploaded[id] ? 0.2 : 1,
              }}
              key={`thumb${index}`}
              className="thumbnail-wrapper"
            >
              <img className="thumbnail" src={src} alt="" />
              <div className="thumbnail-caption">{file.name}</div>
            </div>
          ))}
        </div>
      </form>
    </div>
  )
}

export default App
