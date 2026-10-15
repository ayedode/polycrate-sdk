from typing import Literal

CLIActionRunFinishRequestRequestStatus = Literal["cancelled"]

CLI_ACTION_RUN_FINISH_REQUEST_REQUEST_STATUS_VALUES: set[CLIActionRunFinishRequestRequestStatus] = {
    "cancelled",
}


def check_cli_action_run_finish_request_request_status(value: str) -> CLIActionRunFinishRequestRequestStatus:
    if value in CLI_ACTION_RUN_FINISH_REQUEST_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLI_ACTION_RUN_FINISH_REQUEST_REQUEST_STATUS_VALUES!r}"
    )
