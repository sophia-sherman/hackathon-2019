import React, { Component } from 'react';
import drawPerf from './drawPerf';

export default class LineChartPerf extends Component {

    componentDidMount() {
        drawPerf(this.props);
    }

    componentDidUpdate(preProps) {
        drawPerf(this.props);
    }

    render() {
        console.log(this.props);
        return (
            <div className='linechart-perf'/>
        )
    }
}
