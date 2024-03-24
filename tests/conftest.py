import pytest

from base.utils.database_controller import DataBaseController


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == 'call' or (result.when == 'setup' and result.failed):
        test_name = result.nodeid
        test_path = result.fspath
        if result.failed:
            test_trace = result.longreprtext + "\n" + result.capstdout
        else:
            test_trace = result.capstdout
        test_status = result.outcome
        test_duration = result.duration
        DataBaseController.insert_data(test_name, test_path, test_trace, test_status, test_duration)