import React from 'react';
import {BrowserRouter as Router,Route,Switch} from 'react-router-dom';
import './App.css';
import {Home} from './Home';
import {About} from './About';
import {Contact} from './Contact';
import Watch from './Watch';
import Upload from './Upload';
import Test from './Test';
import {NoMatch} from './NoMatch';
import {Layout} from './components/Layout';
import {NavigationBar} from './components/NaviBar';

function App() {
  return (
    <React.Fragment>
      <NavigationBar />
      <Layout>
        <Router>
          <Switch> //props.children
            <Route  exact path="/" component={Home}/>
            <Route  path="/about" component={About}/>
            <Route  path="/contact" component={Contact}/>
            <Route path="/watch" component={Watch}/>
            <Route path="/upload" component={Upload}/>
            <Route path="/test" component={Test}/>
            <Route  component={NoMatch}/>
          </Switch>
        </Router>
      </Layout>
    </React.Fragment>
  );
}

export default App;
