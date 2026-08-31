from typing import Literal

ApiV1BackupsBackupsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_BACKUPS_BACKUPS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BackupsBackupsUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_backups_backups_update_name_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateNameErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
