import React, { Component } from 'react';
import { Layout } from 'antd';
import axios from 'axios';
import { Logo  } from './images/logo.png';
import Pane1 from './components/Pane1/pane1';
import Pane2 from './components/Pane2/pane2';
import Pane3 from './components/Pane3/pane3';
import './Dashboard.css';

const { Header, Sider, Content, Footer } = Layout;

export default class Dashboard extends Component {

    constructor(props) {
        super(props);
        this.state = {
            repo: "charli-app-mobile",
            coverage: [],
            loading: true
        }
    }

    componentDidMount() {
        let repo = this.state.repo;
        axios.get(`http://127.0.0.1:5000/search?projectKeys=${repo}`, {})
        .then(res =>{
            const report_history = res.data.measures[0].report_history;
            console.log(report_history);
            this.setState({
                coverage: report_history,
                loading: false
            });
        })
        .catch((error)=>{
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
                <div>Loading</div>
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
                        <Sider width={300} style={{backgroundColor:'#eee'}}>
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
                            <Content style={{ height: 200 }}>
                                <Pane2 data={this.state.coverage}/>
                            </Content>
                            <Content style={{ height: 200 }}>
                                <Pane2 data={this.state.coverage}/>
                            </Content>
                        </Layout>
                        <Layout style={{ width: 200 }}>
                            <Content style={{ height: 200 }}>
                                <Pane3 data={this.state.coverage}/>
                            </Content>
                            <Content style={{ height: 200 }}>
                                <Pane3 data={this.state.coverage}/>
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
