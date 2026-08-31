from typing import Literal

ApiV1NotificationsSinksArchiveCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksArchiveCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_archive_create_platform_service_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksArchiveCreatePlatformServiceErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
