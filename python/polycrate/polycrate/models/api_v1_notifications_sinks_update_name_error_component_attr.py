from typing import Literal

ApiV1NotificationsSinksUpdateNameErrorComponentAttr = Literal["name"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_notifications_sinks_update_name_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksUpdateNameErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
