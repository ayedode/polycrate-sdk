from typing import Literal

ApiV1NotificationsSinksUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_notifications_sinks_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
