from typing import Literal

ApiV1BackupsBackupsListTimeRange = Literal["12h", "1h", "24h", "30d", "6h", "7d", "90d"]

API_V1_BACKUPS_BACKUPS_LIST_TIME_RANGE_VALUES: set[ApiV1BackupsBackupsListTimeRange] = {
    "12h",
    "1h",
    "24h",
    "30d",
    "6h",
    "7d",
    "90d",
}


def check_api_v1_backups_backups_list_time_range(value: str) -> ApiV1BackupsBackupsListTimeRange:
    if value in API_V1_BACKUPS_BACKUPS_LIST_TIME_RANGE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_TIME_RANGE_VALUES!r}")
