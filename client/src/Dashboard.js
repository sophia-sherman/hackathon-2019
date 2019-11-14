import React, { Component } from 'react';
import { Layout } from 'antd';
import axios from 'axios';
import { Logo  } from './images/logo.png';
import Pane1 from './components/Pane1/pane1';
import Pane2 from './components/Pane2/pane2';
import Pane3 from './components/Pane3/pane3';
import JiraBugs from './components/JiraBugs/jirabugs';
import './Dashboard.css';

const { Header, Sider, Content, Footer } = Layout;

export default class Dashboard extends Component {

    constructor(props) {
        super(props);
        this.state = {
            // repo: "charli-app-mobile",
            cam_coverage: [],
            cas_coverage: [],
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

        const requestCAM = axios.get(cam);
        const requestCAS = axios.get(cas);
        const bugs = axios.get(jira);

        axios.all([requestCAM, requestCAS, bugs
        ])
        .then(axios.spread((cam, cas, bugs) => {
            const cam_report_history = cam.data.measures[0].report_history;
            const cas_report_history = cas.data.measures[0].report_history;
            const jira_bugs = bugs.data.measures[0];
            this.setState({
                cam_coverage: cam_report_history,
                cas_coverage: cas_report_history,
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
            console.log(this.state);
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
                        <Sider width={300} style={{backgroundColor:'#eee'}}>
                            <Content style={{ height: 200 }}>
                                <div className="sidebar">
                                    <div className="generic-label">Bugs</div>
                                </div>
                            </Content>
                            <Content style={{ height: 300 }}>
                                {/* <Pane1 changeRepo={this.changeRepo}/> */}
                                <div className="sidebar">
                                    <div className="generic-label">Code Coverage</div>
                                    <div className="repo-label">charli-app-mobile</div>
                                </div>
                            </Content>
                            <Content style={{ height: 300 }}>
                                <div className="sidebar">
                                    <div className="generic-label">Code Coverage</div>
                                    <div className="repo-label">charli-app-service</div>
                                </div>
                            </Content>
                            {/* <Content style={{ height: 470 }}>
                            </Content> */}
                        </Sider>
                        <Layout>
                            <Content style={{ height: 210 }}>
                                <JiraBugs data={this.state.jira_bugs}/>
                            </Content>
                            <Layout>
                                <Content style={{ height: 310 }}>
                                    <Pane2 data={this.state.cam_coverage} type={this.state.cam_type}/>
                                </Content>
                                <Content style={{ height: 310 }}>
                                    <Pane2 data={this.state.cas_coverage} type={this.state.cas_type}/>
                                </Content>
                            </Layout>
                        </Layout>
                        <Layout style={{ width: 200 }}>
                            <Content style={{ height: 210 }}>
                            </Content>
                            <Content style={{ height: 310 }}>
                                <Pane3 data={this.state.cam_coverage} type={this.state.cam_type}/>
                            </Content>
                            <Content style={{ height: 310 }}>
                                <Pane3 data={this.state.cas_coverage} type={this.state.cas_type}/>
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
