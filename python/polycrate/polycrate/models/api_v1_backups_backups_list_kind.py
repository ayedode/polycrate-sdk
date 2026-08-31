from typing import Literal

ApiV1BackupsBackupsListKind = Literal["app", "cluster", "database"]

API_V1_BACKUPS_BACKUPS_LIST_KIND_VALUES: set[ApiV1BackupsBackupsListKind] = {
    "app",
    "cluster",
    "database",
}


def check_api_v1_backups_backups_list_kind(value: str) -> ApiV1BackupsBackupsListKind:
    if value in API_V1_BACKUPS_BACKUPS_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_KIND_VALUES!r}")
