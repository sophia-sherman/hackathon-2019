from jira import JIRA

auth_jira = JIRA(basic_auth=('jcoombs', 'Z=[w!ouu2W?i'), options={'server':'https://jira.healthsparq.net'})
# issues = auth_jira.search_issues(jql, fields=['key','priority'], json_result=True)

def count_open_critical_major_issues():
    open_critical_major_jql = 'project in ("CCS Janus Platform", "Product: Janus Platform", "Product: Seamless UX", "Product: Journi") AND issuetype = Bug AND status not in (closed, resolved, Done, "PO Approval", Approved) AND priority in (Blocker, Critical, Major) AND resolution = Unresolved'
    return count_issues(open_critical_major_jql)

def count_open_regression_issues():
    open_regression_jql = 'project in ("CCS Janus Platform",  "Product: Janus Platform", "Product: Journi", "Product: Seamless UX")  AND status not in (closed, resolved, Done, "PO Approval", Approved) AND ((issuetype = Bug AND "Regression Item?" = Yes) OR issuetype = "CCS Incident" ) AND resolution = Unresolved'
    return count_issues(open_regression_jql)

def count_open_data_issues():
    open_data_issues_jql = 'project in ("Product: Seamless UX", "Product: Journi") AND labels = data-quality-impact AND resolution = Unresolved'
    return count_issues(open_data_issues_jql)

def count_open_issues():
    open_issues_jql = 'project in ("Product: Seamless UX", "Product: Journi") AND issuetype = Bug AND status not in (closed, resolved, Done, "PO Approval", Approved) AND resolution = Unresolved'
    return count_issues(open_issues_jql)

def count_issues(jql):
    issues = auth_jira.search_issues(open_regression_jql, fields=['key'])
    return issues.total