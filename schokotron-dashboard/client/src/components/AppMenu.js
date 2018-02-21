import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import AppBar from 'material-ui/AppBar';

const ROUTES = {
    '/': 'Dashboard',
    '/users': 'Users',
    '/feeds': 'Feeds'
  };
  
  export class AppMenu extends Component {
    static displayName = 'AppMenu';
    static propTypes = {
      location: PropTypes.object.isRequired,
    };
  
    constructor(props) {
      this.state = {open: false};
      super(props);
    }

    getMainTabBar() {
        return (
            <AppBar
                title="Schokotron Dashboard"
                onLeftIconButtonTouchTap={this.toggleNavigation}
            />
        );
    }

    getTabs() {
        const { location } = this.props;
        return Object.keys(ROUTES).map((route, i) => {
            return (
                <Link
                    key={i}
                    className="nav-link"
                    active={location.pathname === route}
                    to={route}
                    onTouchTap={() => this.toggleNavigation}
                >
                    <MenuItem>{ROUTES[route]}</MenuItem>
                </Link>
            );
        });
    }

    getDrawer() {
        return (
            <Drawer
                open={this.state.open}
                docked={false}
                onRequestChange={(open) => this.setState({ open })}
            >
            <AppBar
                title="RMD"
                showMenuIconButton={false}
                titleStyle={navTitleStyle}
            />
            {this.getTabs()}
            </Drawer>
        );
    }

    toggleNavigation() {
        this.setState({open: !this.state.open});
    }
  
    render() {
      return (
        <div id="main">
          <AppBar
            title="React Material Dashboard"
            onLeftIconButtonTouchTap={this.toggleNavigation}
            iconElementRight={githubButton}
          />
          {this.getDrawer()}
        <div className="page-content">
          {this.props.children}
        </div>
      </div>
      );
  }
}
  
export default AppMenu;