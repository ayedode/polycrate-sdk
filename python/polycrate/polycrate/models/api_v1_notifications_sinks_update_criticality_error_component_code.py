from typing import Literal

ApiV1NotificationsSinksUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_notifications_sinks_update_criticality_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksUpdateCriticalityErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
