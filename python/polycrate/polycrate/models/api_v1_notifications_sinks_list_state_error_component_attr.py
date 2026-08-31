from typing import Literal

ApiV1NotificationsSinksListStateErrorComponentAttr = Literal["state"]

API_V1_NOTIFICATIONS_SINKS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_notifications_sinks_list_state_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksListStateErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
