import React, { Component } from 'react';
import './pane2.css';
import LineChart from '../../charts/LineChart/linechart';

export default class Pane2 extends Component {
    render() {
        const {data} = this.props,
              width = 650,
              height = 250;
        return (
            <div id="pane2" className="pane" >
                <div className='header'>Code Coverage</div>
                <div style={{ overflowX: 'scroll',overflowY:'hidden' }}>
                    <LineChart data={data} width={width} height={height}/>
                </div>
            </div>
        )
    }
}