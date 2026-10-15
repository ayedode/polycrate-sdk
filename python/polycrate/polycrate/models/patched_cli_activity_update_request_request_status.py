from typing import Literal

PatchedCLIActivityUpdateRequestRequestStatus = Literal["failed", "success"]

PATCHED_CLI_ACTIVITY_UPDATE_REQUEST_REQUEST_STATUS_VALUES: set[PatchedCLIActivityUpdateRequestRequestStatus] = {
    "failed",
    "success",
}


def check_patched_cli_activity_update_request_request_status(
    value: str,
) -> PatchedCLIActivityUpdateRequestRequestStatus:
    if value in PATCHED_CLI_ACTIVITY_UPDATE_REQUEST_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_CLI_ACTIVITY_UPDATE_REQUEST_REQUEST_STATUS_VALUES!r}"
    )
