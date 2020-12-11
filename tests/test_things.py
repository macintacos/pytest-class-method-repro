import pytest
from app import FakeJira
from jira import JIRA


def test_get_jira_issue(mocker):
    def __init__(self):
        self.jira = JIRA()

    mocker.patch.object(JIRA, "__init__", autospec=True, return_value=None)
    mocker.patch.object(
        JIRA,
        "issue",
        return_value={"hey": "I ACTUALLY RETURNED IN THE RIGHT CALL HALLELUJAH"},
    )
    mocker.patch.object(FakeJira, "__init__", __init__)

    hey = FakeJira()

    issue = hey.get_jira_issue("some issue")

    assert issue == {
        "code": "the call actually succeeded, but I need to mock issue.raw and idk how",
        "issue": "",
        "this": "never gets called",
    }
