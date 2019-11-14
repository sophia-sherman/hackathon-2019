import React, { Component } from 'react';
import drawCAS from './drawCAS';

export default class LineChart extends Component {

    componentDidMount() {
        drawCAS(this.props);
    }

    componentDidUpdate(preProps) {
        drawCAS(this.props);
    }

    render() {
        return (
            <div className='linechart-cas'/>
        )
    }
}
