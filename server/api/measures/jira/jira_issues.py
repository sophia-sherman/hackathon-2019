from jira import JIRA

auth_jira = JIRA(basic_auth=('jcoombs', 'Z=[w!ouu2W?i'), options={'server': 'https://jira.healthsparq.net'})

# issues = auth_jira.search_issues(jql, fields=['key','priority'], json_result=True)

def count_open_critical_major_issues():
    # open_critical_major_jql = 'project in ("CCS Janus Platform", "Product: Janus Platform", "Product: Seamless UX", "Product: Journi") AND issuetype = Bug AND status not in (closed, resolved, Done, "PO Approval", Approved) AND priority in (Blocker, Critical, Major) AND resolution = Unresolved'
    open_critical_major_jql = 'project = SEAM AND issuetype = Bug AND (priority = Critical OR priority = Major) AND ' \
                              'status != Closed'
    return count_issues(open_critical_major_jql)


def count_open_regression_issues():
    # open_regression_jql = 'project in ("CCS Janus Platform",  "Product: Janus Platform", "Product: Journi", "Product: Seamless UX")  AND status not in (closed, resolved, Done, "PO Approval", Approved) AND ((issuetype = Bug AND "Regression Item?" = Yes) OR issuetype = "CCS Incident" ) AND resolution = Unresolved'
    open_regression_jql = 'project = SEAM AND issuetype = "CCS Incident" AND status != Closed'
    return count_issues(open_regression_jql)


def count_open_data_issues():
    # open_data_issues_jql = 'project in ("Product: Seamless UX", "Product: Journi") AND labels = data-quality-impact AND resolution = Unresolved'
    open_data_issues_jql = 'project = SEAM AND status !=  Closed AND labels = data-quality-impact'
    return count_issues(open_data_issues_jql)


def count_open_issues():
    # open_issues_jql = 'project in ("Product: Seamless UX", "Product: Journi") AND issuetype = Bug AND status not in (closed, resolved, Done, "PO Approval", Approved) AND resolution = Unresolved'
    open_issues_jql = 'project = SEAM AND issuetype = Bug AND status != Closed'
    return count_issues(open_issues_jql)


def count_opened_issues_in_sprint():
    opened_issues_jql = 'project = SEAM AND issuetype = Bug AND created >= 2019-10-30 AND created <= 2019-11-13'
    return count_issues(opened_issues_jql)


def count_closed_issues_in_sprint():
    closed_issues_jql = 'project = SEAM AND issuetype = Bug AND status = Closed AND resolved >= 2019-10-30 AND resolved <= 2019-11-13'
    return count_issues(closed_issues_jql)


def count_issues(jql):
    issues = auth_jira.search_issues(jql, fields=['key'])
    return issues.total
