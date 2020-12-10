import pytest
from app import FakeJira
from jira import JIRA


def test_get_jira_issue(mocker):
    mocker.patch.object(JIRA, "__init__", autospec=True, return_value=None)
    mocker.patch.object(
        JIRA,
        "issue",
        return_value={"hey": "I ACTUALLY RETURNED IN THE RIGHT CALL HALLELUJAH"},
    )

    def __init__(self):
        self.jira = JIRA()

    mocker.patch.object(FakeJira, "__init__", __init__)

    hey = FakeJira()
    the_issue_call_works_i_swear = JIRA.issue()

    issue = hey.get_jira_issue("some issue")

    assert issue == the_issue_call_works_i_swear
