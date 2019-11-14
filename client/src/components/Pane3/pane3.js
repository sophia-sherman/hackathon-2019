import React, { Component } from 'react';
import { Icon } from 'antd';
import './pane3.css';

export default class View5 extends Component {
    render() {
        const {data} = this.props;
        const sorted = data.sort((d1, d2) => new Date(d1.source_date).getTime() - new Date(d2.source_date).getTime());
        const final = sorted.reverse();
        const test = final[0];
        return (
            <div id="pane3" className="pane">
                <div className="header">Latest Code Coverage</div>
                <div className="latest">
                    <div className="percent">
                        {test.stmts}%
                    </div>
                    <Icon type="arrow-up" />
                </div>               
            </div>
        )
    }
}