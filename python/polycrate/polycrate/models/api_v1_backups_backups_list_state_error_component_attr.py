from typing import Literal

ApiV1BackupsBackupsListStateErrorComponentAttr = Literal["state"]

API_V1_BACKUPS_BACKUPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BackupsBackupsListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_backups_backups_list_state_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsListStateErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
