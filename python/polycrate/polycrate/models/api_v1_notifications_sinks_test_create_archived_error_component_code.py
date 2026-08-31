from typing import Literal

ApiV1NotificationsSinksTestCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksTestCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_test_create_archived_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksTestCreateArchivedErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
