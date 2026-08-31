from typing import Literal

ApiV1NotificationsSinksArchiveCreateIsSystemDefaultErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksArchiveCreateIsSystemDefaultErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_archive_create_is_system_default_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksArchiveCreateIsSystemDefaultErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
