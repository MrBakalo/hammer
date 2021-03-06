import pytest


from . import mock_iam
from datetime import datetime, timedelta, timezone
from library.aws.iam import IAMKeyChecker
from library.aws.utility import Account


# starting point for checking if key expired
now = datetime.now(timezone.utc)
# criteria for checking if key expired
rotation_criteria_days = timedelta(days=10)

# mocked AWS IAM environment
users = {
    "User1": {
        "Keys": [
            {
                "Description": "Key on a half way to expiration",
                "CreateDate": now - rotation_criteria_days / 2,
                "Active": True,
                "CheckShouldPass": True
            },
            {
                "Description": "Not active key",
                "CreateDate": now - rotation_criteria_days - timedelta(minutes=1),
                "Active": False,
                "CheckShouldPass": True
            }
        ]
    },
    "User2": {
        "Keys": [
            {
                "Description": "Key with one minute before expiration",
                "CreateDate": now - rotation_criteria_days + timedelta(minutes=1),
                "Active": True,
                "CheckShouldPass": True
            },
            {
                "Description": "Key expired one minute ago",
                "CreateDate": now - rotation_criteria_days - timedelta(minutes=1),
                "Active": True,
                "CheckShouldPass": False
            }
        ]
    }
}


def ident_test(key):
    """
    Used to build identification string for each autogenerated test (for easy recognition of failed tests).

    :param keyRotation_details: dict with information about access key from
                        describe_iam_accesskeyRotation_details.validate_user_inactive_keys(...)
    :return: identification string with user name, key index number and human-readable description.
    """
    descr = mock_iam.find_key_prop(users, key, "Description", "default description")
    indx = mock_iam.find_key_prop(users, key, "TestId", "0")
    return f"params: {key.user.id}.{indx} ({descr})"


def pytest_generate_tests(metafunc):
    """
    Entrypoint for tests (built-in pytest function for dynamic generation of test cases).
    """
    # Launch IAM mocking and env preparation
    mock_iam.start()
    mock_iam.create_env(users)

    account = Account()

    # validate user expired keys in mocked env
    checker = IAMKeyChecker(account,
                            now=now,
                            rotation_criteria_days=rotation_criteria_days)
    checker.check(last_used_check_enabled=False)
    keys = []
    for user in checker.users:
        keys += user.keys

    # create test cases for each key
    metafunc.parametrize("key", keys, ids=ident_test)


@pytest.mark.iamRotation
def test_keyRotation(key):
    """
    Actual testing function.

    :param keyRotation_details: dict with information about access key from
                        describe_iam_accesskeyRotation_details.validate_user_inactive_keys(...)
    :return: nothing, raises AssertionError if actual test result is not matched with expected
    """
    #print(f"{json.dumps(keyRotation_details, indent=4, default = jsonEncoder)}")
    expected = mock_iam.find_key_prop(users, key, "CheckShouldPass", True)
    assert expected == (not key.stale)