from typing import Literal

ApiV1BackupsBackupsListStatus = Literal["completed", "expired", "failed", "partial", "pending", "running", "unknown"]

API_V1_BACKUPS_BACKUPS_LIST_STATUS_VALUES: set[ApiV1BackupsBackupsListStatus] = {
    "completed",
    "expired",
    "failed",
    "partial",
    "pending",
    "running",
    "unknown",
}


def check_api_v1_backups_backups_list_status(value: str) -> ApiV1BackupsBackupsListStatus:
    if value in API_V1_BACKUPS_BACKUPS_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_STATUS_VALUES!r}")
