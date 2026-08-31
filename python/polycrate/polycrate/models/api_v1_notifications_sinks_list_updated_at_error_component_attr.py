from typing import Literal

ApiV1NotificationsSinksListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_NOTIFICATIONS_SINKS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_notifications_sinks_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksListUpdatedAtErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
