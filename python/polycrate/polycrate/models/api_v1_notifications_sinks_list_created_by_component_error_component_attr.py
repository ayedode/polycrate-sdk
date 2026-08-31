from typing import Literal

ApiV1NotificationsSinksListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_NOTIFICATIONS_SINKS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_notifications_sinks_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksListCreatedByComponentErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
