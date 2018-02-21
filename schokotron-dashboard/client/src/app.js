import React from "react";
import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";
import Dashboard from './containers/dashboard';
import Users from './containers/users';
import Feeds from './containers/feeds';




const DashboardSchokotronApp = () => (
    <Router>
        <Route exact path="/" component={Dashboard} />
        <Route exact path="/settings" component={SettingsWithTracking} />
        {isDev && <Route exact path="/styleguide/:page?" component={StyleGuide} />}
        <Miss />
    </Router>
  );
  
  export default ExecutivesApp;
  