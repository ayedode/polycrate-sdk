from typing import Literal

ApiV1NotificationsSinksTestCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksTestCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_notifications_sinks_test_create_archived_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksTestCreateArchivedErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
