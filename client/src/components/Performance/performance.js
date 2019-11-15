import React, { Component } from 'react';
import { Table } from 'antd';
import './performance.css';

const columns = [
    {
        title: 'Mean Response time (ms)',
        dataIndex: 'response',
        key: 'response',
    },
    {
        title: 'Req/sec',
        dataIndex: 'request',
        key: 'request',
    },
    {
        title: 'Error Rate (%)',
        dataIndex: 'ko',
        key: 'ko',
    }
];

export default class Performance extends Component {
    render() {
        const {data} = this.props;
        const sorted = (data.sort((d1, d2) => new Date(d1.source_date).getTime() - new Date(d2.source_date).getTime())).reverse();
        const recent_perf_metrics = sorted[0];
        const dataSource = [
            {
                key: '1',
                response: recent_perf_metrics.value.response_mean,
                request: recent_perf_metrics.value.request_mean,
                ko: recent_perf_metrics.value.ko_percent,
              },
        ];
        return (
            <div id="perf" className="pane">
                <div className="header">Jira Bugs</div>
                <Table columns={columns} dataSource={dataSource} pagination={false}  />
            </div>
        )
    }
}
