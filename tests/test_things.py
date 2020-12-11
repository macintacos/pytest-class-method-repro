from app import FakeJira
from jira import JIRA
from mock import patch


def test_get_jira_issue(mocker):
    def __init__(self):
        self.jira = JIRA()

    mocker.patch.object(JIRA, "__init__", autospec=True, return_value=None)
    mocker.patch.object(FakeJira, "__init__", __init__)
    with patch("jira.JIRA.issue") as mock_issue:
        issue = JIRA.issue()
        issue.raw = "it works!"
        mock_issue.return_value = issue

        hey = FakeJira()
        issue = hey.get_jira_issue("some issue")

        assert issue == {
            "code": "the call actually succeeded, but I need to mock issue.raw and idk how",
            "issue": "it works!",
            "this": "never gets called",
        }
