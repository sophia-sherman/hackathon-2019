import React, { Component } from 'react';
import { Icon } from 'antd';
import './indicator.css';

export default class Indicator extends Component {
    render() {
        const { type } = this.props;
        if (type === 'jest') {
            return (
                <div id="indicator" className="pane">
                    <div className="header">Smoke Test Pass Rate</div>
                    <div className="latest">
                        <div className="indicator-percent">
                            42%
                        </div>
                        <Icon type="arrow-up" />
                    </div>               
                </div>
            )
        }
        else {
            return (
                <div id="indicator" className="pane">
                    <div className="header">Feature Coverage</div>
                    <div className="latest">
                        <div className="indicator-percent">
                            100%
                        </div>
                        <Icon type="arrow-up" />
                    </div>               
                </div>
            )
        }
    }
}