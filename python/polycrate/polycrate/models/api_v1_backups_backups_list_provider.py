from typing import Literal

ApiV1BackupsBackupsListProvider = Literal["cloudnativepg", "custom", "velero"]

API_V1_BACKUPS_BACKUPS_LIST_PROVIDER_VALUES: set[ApiV1BackupsBackupsListProvider] = {
    "cloudnativepg",
    "custom",
    "velero",
}


def check_api_v1_backups_backups_list_provider(value: str) -> ApiV1BackupsBackupsListProvider:
    if value in API_V1_BACKUPS_BACKUPS_LIST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_PROVIDER_VALUES!r}")
