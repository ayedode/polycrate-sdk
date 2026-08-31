from typing import Literal

ApiV1NotificationsSinksCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_create_archived_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksCreateArchivedErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
