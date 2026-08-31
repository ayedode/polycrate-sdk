from typing import Literal

ApiV1BackupsBackupsListScope = Literal["system", "user"]

API_V1_BACKUPS_BACKUPS_LIST_SCOPE_VALUES: set[ApiV1BackupsBackupsListScope] = {
    "system",
    "user",
}


def check_api_v1_backups_backups_list_scope(value: str) -> ApiV1BackupsBackupsListScope:
    if value in API_V1_BACKUPS_BACKUPS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_SCOPE_VALUES!r}")
