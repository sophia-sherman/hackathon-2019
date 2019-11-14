import React, { Component } from 'react';
import './pane2.css';
import LineChartCAS from '../../charts/LineChart/linechartCAS';
import LineChartCAM from '../../charts/LineChart/linechart';

export default class Pane2 extends Component {
    render() {
        const {data, type} = this.props,
              width = 650,
              height = 250;
        if (type === 'jest') {
            return (
                <div id="pane2" className="pane" >
                    <div className='header'>Code Coverage</div>
                    <div style={{ overflowX: 'scroll',overflowY:'hidden' }}>
                        <LineChartCAM data={data} width={width} height={height}/>
                    </div>
                </div>
            )
        }
        else {
            return (
                <div id="pane2" className="pane" >
                    <div className='header'>Code Coverage</div>
                    <div style={{ overflowX: 'scroll',overflowY:'hidden' }}>
                        <LineChartCAS data={data} width={width} height={height}/>
                    </div>
                </div>
            )
        }  
    }
}