import React, { Component } from 'react';
import { Table } from 'antd';
import './jirabugs.css';

const columns = [
    {
        title: 'Open Crit/Major',
        dataIndex: 'critical',
        key: 'critical',
    },
    {
        title: 'Open Regression',
        dataIndex: 'regression',
        key: 'regression',
    },
    {
        title: 'Open Quality',
        dataIndex: 'quality',
        key: 'quality',
    },
    {
        title: 'Opened in Last Sprint',
        dataIndex: 'opened_sprint',
        key: 'opened_sprint',
    },
    {
        title: 'Closed in Last Sprint',
        dataIndex: 'closed_sprint',
        key: 'closed_sprint',
    },
    {
        title: 'Total Open',
        dataIndex: 'total',
        key: 'total',
    },
];

export default class JiraBugs extends Component {
    render() {
        const {data} = this.props;
        const dataSource = [
            {
                key: '1',
                critical: data.open_critical_major_bugs,
                regression: data.open_regressions,
                quality: data.open_data_quality_bugs,
                opened_sprint: data.opened_during_sprint,
                closed_sprint: data.closed_during_sprint,
                total: data.total_open_bugs
              },
        ];
        return (
            <div id="jira" className="pane">
                <div className="header">Jira Bugs</div>
                <Table columns={columns} dataSource={dataSource} pagination={false}  />
            </div>
        )
    }
}
