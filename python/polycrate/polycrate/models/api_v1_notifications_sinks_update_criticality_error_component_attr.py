from typing import Literal

ApiV1NotificationsSinksUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_notifications_sinks_update_criticality_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksUpdateCriticalityErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
