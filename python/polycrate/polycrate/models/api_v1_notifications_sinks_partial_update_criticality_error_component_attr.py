from typing import Literal

ApiV1NotificationsSinksPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_notifications_sinks_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
