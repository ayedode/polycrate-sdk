from typing import Literal

ApiV1NotificationsSinksUpdateConfigErrorComponentAttr = Literal["config"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksUpdateConfigErrorComponentAttr
] = {
    "config",
}


def check_api_v1_notifications_sinks_update_config_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksUpdateConfigErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
