from typing import Literal

ApiV1NotificationsSinksTestCreateConfigErrorComponentAttr = Literal["config"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksTestCreateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_notifications_sinks_test_create_config_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksTestCreateConfigErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
