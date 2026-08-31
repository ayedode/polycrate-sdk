from typing import Literal

ApiV1BackupsBackupsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BACKUPS_BACKUPS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_backups_backups_update_criticality_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
