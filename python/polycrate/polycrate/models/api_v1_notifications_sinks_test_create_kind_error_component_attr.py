from typing import Literal

ApiV1NotificationsSinksTestCreateKindErrorComponentAttr = Literal["kind"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksTestCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_notifications_sinks_test_create_kind_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksTestCreateKindErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
