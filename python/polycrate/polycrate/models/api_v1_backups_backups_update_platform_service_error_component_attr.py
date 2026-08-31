from typing import Literal

ApiV1BackupsBackupsUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_BACKUPS_BACKUPS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_backups_backups_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
