from typing import Literal

ApiV1NotificationsSinksTestCreateNameErrorComponentAttr = Literal["name"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksTestCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_notifications_sinks_test_create_name_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksTestCreateNameErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
