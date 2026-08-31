from typing import Literal

ApiV1BackupsBackupsListStatusErrorComponentAttr = Literal["status"]

API_V1_BACKUPS_BACKUPS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BackupsBackupsListStatusErrorComponentAttr] = {
    "status",
}


def check_api_v1_backups_backups_list_status_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsListStatusErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
