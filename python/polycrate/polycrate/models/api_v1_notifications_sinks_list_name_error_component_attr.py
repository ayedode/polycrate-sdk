from typing import Literal

ApiV1NotificationsSinksListNameErrorComponentAttr = Literal["name"]

API_V1_NOTIFICATIONS_SINKS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksListNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_notifications_sinks_list_name_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksListNameErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
