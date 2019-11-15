import React from 'react';
import ReactDOM from 'react-dom';

var hW1 = React.createElement('h3',null,'Surgeon City')
var hW2 = React.createElement('h3',null,'Initial')

var div1 = React.createElement('div',null,hW1,hW2);

ReactDOM.render(
  div1,
  document.getElementById('app')
)
