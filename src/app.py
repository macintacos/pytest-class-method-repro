import sys

from jira import JIRA
from jira.exceptions import JIRAError

PROD_JIRA_BACKEND = "https://something.jira.org"


class FakeJira(object):
    # setup Jira
    def __init__(self, secret, JIRA_BACKEND=PROD_JIRA_BACKEND):
        self.jira = JIRA(
            options={"server": JIRA_BACKEND},
            oauth={
                "access_token": secret["access_token"],
                "access_token_secret": secret["access_token_secret"],
                "consumer_key": secret["consumer_key"],
                "key_cert": secret["key_cert"],
            },
        )

    def get_jira_issue(self, issue_id):
        """Get issue by ID"""
        response = dict()
        response["code"] = ""

        try:
            issue = self.jira.issue(issue_id)
        except:
            print(sys.exc_info())
            response["code"] = "there was an error even though this should be mocked"
            response["issue"] = "issue is never returned"
        else:
            response[
                "code"
            ] = "the call actually succeeded, but I need to mock issue.raw and idk how"
            response["issue"] = issue.raw
            response["this"] = "never gets called"
        finally:
            return response
