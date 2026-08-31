from typing import Literal

ApiV1NotificationsSinksPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_notifications_sinks_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
