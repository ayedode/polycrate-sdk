from typing import Literal

ApiV1BackupsBackupsUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_BACKUPS_BACKUPS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_backups_backups_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
