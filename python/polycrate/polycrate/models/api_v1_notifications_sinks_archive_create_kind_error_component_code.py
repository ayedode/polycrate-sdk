from typing import Literal

ApiV1NotificationsSinksArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_notifications_sinks_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksArchiveCreateKindErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
