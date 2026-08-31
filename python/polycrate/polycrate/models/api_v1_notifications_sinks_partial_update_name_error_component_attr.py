from typing import Literal

ApiV1NotificationsSinksPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_notifications_sinks_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksPartialUpdateNameErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
