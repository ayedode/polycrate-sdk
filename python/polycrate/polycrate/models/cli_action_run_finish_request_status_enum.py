from typing import Literal

CLIActionRunFinishRequestStatusEnum = Literal["cancelled"]

CLI_ACTION_RUN_FINISH_REQUEST_STATUS_ENUM_VALUES: set[CLIActionRunFinishRequestStatusEnum] = {
    "cancelled",
}


def check_cli_action_run_finish_request_status_enum(value: str) -> CLIActionRunFinishRequestStatusEnum:
    if value in CLI_ACTION_RUN_FINISH_REQUEST_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLI_ACTION_RUN_FINISH_REQUEST_STATUS_ENUM_VALUES!r}")
