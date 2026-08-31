from typing import Literal

ApiV1NotificationsSinksTestCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksTestCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_notifications_sinks_test_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksTestCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
