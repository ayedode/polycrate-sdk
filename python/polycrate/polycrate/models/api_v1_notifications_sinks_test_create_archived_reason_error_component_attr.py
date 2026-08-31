from typing import Literal

ApiV1NotificationsSinksTestCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksTestCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_notifications_sinks_test_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksTestCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
