from typing import Literal

CLIActivityUpdateRequestStatusEnum = Literal["failed", "success"]

CLI_ACTIVITY_UPDATE_REQUEST_STATUS_ENUM_VALUES: set[CLIActivityUpdateRequestStatusEnum] = {
    "failed",
    "success",
}


def check_cli_activity_update_request_status_enum(value: str) -> CLIActivityUpdateRequestStatusEnum:
    if value in CLI_ACTIVITY_UPDATE_REQUEST_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLI_ACTIVITY_UPDATE_REQUEST_STATUS_ENUM_VALUES!r}")
