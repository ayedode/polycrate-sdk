from typing import Literal

ApiV1BackupsBackupsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_BACKUPS_BACKUPS_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1BackupsBackupsListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_backups_backups_list_created_by_component(value: str) -> ApiV1BackupsBackupsListCreatedByComponent:
    if value in API_V1_BACKUPS_BACKUPS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
