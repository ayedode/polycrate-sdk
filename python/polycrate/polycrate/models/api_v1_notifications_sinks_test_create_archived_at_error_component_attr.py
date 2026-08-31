from typing import Literal

ApiV1NotificationsSinksTestCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksTestCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_notifications_sinks_test_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksTestCreateArchivedAtErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
