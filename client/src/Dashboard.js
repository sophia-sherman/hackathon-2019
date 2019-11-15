import React, { Component } from 'react';
import { Layout } from 'antd';
import axios from 'axios';
import Pane2 from './components/Pane2/pane2';
import Pane3 from './components/Pane3/pane3';
import JiraBugs from './components/JiraBugs/jirabugs';
import Performance from './components/Performance/performance';
import Linegraph from './components/Performance/linegraph';
import './Dashboard.css';

const { Header, Sider, Content, Footer } = Layout;

export default class Dashboard extends Component {

    constructor(props) {
        super(props);
        this.state = {
            // repo: "charli-app-mobile",
            cam_coverage: [],
            cas_coverage: [],
            perf_metrics: [],
            cam_type: "jest", 
            cas_type: "cloverage",
            jira_bugs: {},
            loading: true
        }
    }

    componentDidMount() {
        let cam = `http://127.0.0.1:5000/search?projectKeys=charli-app-mobile`
        let cas =  `http://127.0.0.1:5000/search?projectKeys=charli-app-service`
        let jira = `http://127.0.0.1:5000/bugs`
        let gatling = `http://127.0.0.1:5000/performance?projectKeys=charli-app-service`

        const requestCAM = axios.get(cam);
        const requestCAS = axios.get(cas);
        const bugs = axios.get(jira);
        const performance = axios.get(gatling);

        axios.all([requestCAM, requestCAS, bugs, performance
        ])
        .then(axios.spread((cam, cas, bugs, perf) => {
            const cam_report_history = cam.data.measures[0].report_history;
            const cas_report_history = cas.data.measures[0].report_history;
            const jira_bugs = bugs.data.measures[0];
            const perf_metrics =  perf.data.measures[0].report_history;
            this.setState({
                cam_coverage: cam_report_history,
                cas_coverage: cas_report_history,
                perf_metrics: perf_metrics,
                jira_bugs: jira_bugs,
                loading: false
            });
        }))
        .catch((error) => {
            alert(error);
            alert("There is an error in API call.");
        });
    }

    changeRepo = value => {
        this.setState({
            changeRepo: value,
            repo: value
        })
    }

    render() {
        if (this.state.loading){
            return(
                <div>Loading...</div>
            )
        }
        else{
            return (
                <div>
                    <Layout>
                        <Header style={{ height: 20 }}>
                            <div style={{marginTop: -30}}>
                                Dashboard
                            </div>
                        </Header>
                    </Layout>
                    <Layout>
                        <Sider width={200} style={{backgroundColor:'#eee'}}>
                            <Content style={{ height: 220 }}>
                                <div className="sidebar">
                                    <div className="generic-label">Bugs</div>
                                </div>
                            </Content>
                            <Content style={{ height: 310 }}>
                                {/* <Pane1 changeRepo={this.changeRepo}/> */}
                                <div className="sidebar">
                                    <div className="generic-label">Code Coverage</div>
                                    <div className="repo-label">charli-app-mobile</div>
                                </div>
                            </Content>
                            <Content style={{ height: 310 }}>
                                <div className="sidebar">
                                    <div className="generic-label">Code Coverage</div>
                                    <div className="repo-label">charli-app-service</div>
                                </div>
                            </Content>
                            <Content style={{ height: 310 }}>
                                <div className="sidebar">
                                    <div className="generic-label">Performance Metrics</div>
                                    <div className="repo-label">charli-app-service</div>
                                </div>
                            </Content>
                        </Sider>
                        <Layout>
                            <Content style={{ height: 220 }}>
                                <JiraBugs data={this.state.jira_bugs}/>
                            </Content>
                            <Layout>
                                <Content style={{ height: 320 }}>
                                    <Pane2 data={this.state.cam_coverage} type={this.state.cam_type}/>
                                </Content>
                                <Content style={{ height: 320 }}>
                                    <Pane2 data={this.state.cas_coverage} type={this.state.cas_type}/>
                                </Content>
                                <Content style={{ height: 320 }}>
                                    <Linegraph data={this.state.perf_metrics} />
                                </Content>
                            </Layout>
                        </Layout>
                        <Layout style={{ width: 400 }}>
                            <Content style={{ height: 220 }}>
                            </Content>
                            <Content style={{ height: 320 }}>
                                <Pane3 data={this.state.cam_coverage} type={this.state.cam_type}/>
                            </Content>
                            <Content style={{ height: 320 }}>
                                <Pane3 data={this.state.cas_coverage} type={this.state.cas_type}/>
                            </Content>
                            <Content style={{ height: 320 }}>
                                <Performance data={this.state.perf_metrics}/>
                            </Content>
                        </Layout>
                    </Layout>
                    <Layout>
                        <Footer style={{ height: 20 }}>
                            <div style={{marginTop: -10}}>
                                Cambia Hackathon 2019
                            </div>
                        </Footer>
                    </Layout>
                </div>
            ) 
        }

    }
}
