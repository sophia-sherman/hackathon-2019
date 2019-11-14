import React, { Component } from 'react';
import { Menu, Dropdown, Icon } from 'antd';
import './pane1.css';

const menuItems = [
    {
      key: 1,
      value: "charli-app-mobile"
    },
    {
      key: 2,
      value: "charli-app-service"
    }
];

export default class Pane1 extends Component {
    constructor(props) {
        super(props);
        this.state = {
            selected: "charli-app-mobile"
        };
    }

    handleMenuClick = e => {
        const newSelected = menuItems.find(item => item.key === parseInt(e.key, 10))
          .value;
        this.setState({selected: newSelected});
        this.props.changeRepo(newSelected);
    };

    menu = (
        <Menu onClick={this.handleMenuClick}>
          {menuItems.map(item => (
            <Menu.Item key={item.key}>{item.value}</Menu.Item>
          ))}
        </Menu>
    );

    render() {
        return (
            <div id="pane1" className="pane">
                <div className="header">Filter</div>
                <div>
                    <div className="info-view">
                        <Dropdown overlay={this.menu} trigger={["click"]}>
                            <a className="ant-dropdown-link" href="#">
                                {this.state.selected} <Icon type="down" />
                            </a>
                        </Dropdown>
                    </div>
                </div>
            </div>
        )
    }
}
