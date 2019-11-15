import React, { Component } from 'react';
import './linegraph.css';
import LineChartPerf from '../../charts/LineChart/linechartPerf';

export default class Linegraph extends Component {
    render() {
        const {data} = this.props,
              width = 800,
              height = 250;
        return (
            <div id="perf-line" className="pane" >
                <div className='header'>Performance Test History</div>
                <div style={{ overflowX: 'scroll',overflowY:'hidden' }}>
                    <LineChartPerf data={data} width={width} height={height}/>
                </div>
            </div>
        )
    }
}