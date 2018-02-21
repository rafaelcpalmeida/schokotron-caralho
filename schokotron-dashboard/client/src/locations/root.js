import React from 'react';
import {AppBar, Drawer} from 'material-ui';


class Layout extends React.Component {
    constructor(props) {
      super(props);
      this.state = {open: false};
      this.toggleNavigation = this.toggleNavigation.bind(this);
    }
  
    toggleNavigation() {
      this.setState({open: !this.state.open});
    }
  
    render() {
      var navTitleStyle = {
        marginLeft: '-8px'
      };
  
      return (
        <div id="main">
          <AppBar
            title="React Material Dashboard"
            onLeftIconButtonTouchTap={this.toggleNavigation}
            iconElementRight={githubButton}
          />
          <Drawer
            open={this.state.open}
            docked={false}
            onRequestChange={(open) => this.setState({open})}
          >
            <AppBar
              title="Schokotron"
              showMenuIconButton={false}
              titleStyle={navTitleStyle}
            />
            {this.props.links}
          </Drawer>
          <div className="page-content">
            {this.props.children}
          </div>
        </div>
      );
    }
  }
  
  
  export default Layout;
