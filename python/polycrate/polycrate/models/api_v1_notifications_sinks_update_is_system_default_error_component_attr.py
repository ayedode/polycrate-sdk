from typing import Literal

ApiV1NotificationsSinksUpdateIsSystemDefaultErrorComponentAttr = Literal["is_system_default"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksUpdateIsSystemDefaultErrorComponentAttr
] = {
    "is_system_default",
}


def check_api_v1_notifications_sinks_update_is_system_default_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksUpdateIsSystemDefaultErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_IS_SYSTEM_DEFAULT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
