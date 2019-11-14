import React, { Component } from 'react';
import { Icon } from 'antd';
import './pane3.css';

export default class Pane3 extends Component {
    render() {
        const {data} = this.props;
        const sorted = (data.sort((d1, d2) => new Date(d1.source_date).getTime() - new Date(d2.source_date).getTime())).reverse();
        const percent = sorted[0];
        // check if we should have an up arrow or down arrow
        if (sorted[0].value > sorted[1].value) {
            return (
                <div id="pane3" className="pane">
                    <div className="header">Latest Code Coverage</div>
                    <div className="latest">
                        <div className="percent">
                            {percent.value}%
                        </div>
                        <Icon type="arrow-up" />
                    </div>               
                </div>
            )
        }
        else {
            return (
                <div id="pane3" className="pane">
                    <div className="header">Latest Code Coverage</div>
                    <div className="latest">
                        <div className="percent">
                            {percent.value}%
                        </div>
                        <Icon type="arrow-down" />
                    </div>               
                </div>
            )
        } 
    }
}