import React from 'react';
import {Jumbotron as Jumbo, Container} from 'react-bootstrap';
import styled from 'styled-components';
import eyeimage from '../assests/eyeSurgery.jpg';

const Styles = styled.div`
  .jumbtron{
    background: url(${eyeSurgery}) no-repeat fixed bottom;
    background-size: cover;
    color: #ccc;
    height:200px;
    position: relative;
    z-index: -2;
  }
  .overlay{
    background-color: #000;
    opacity:0.6;
    position:absolute;
    top:0
    bottom:0
    right:0
    z-index:-1;
  }
`;


export const Jumbotron = () => (
  <Styles>
    <Jumbo fluid classname="jumbo">
      <div classname="overlay"></div>
      <Container>
        <h1>Welcome to Surgeon City</h1>
        <p>Upload a video to get a highlight</p>
      </Container>
    </Jumbo>
  </Styles>

)
