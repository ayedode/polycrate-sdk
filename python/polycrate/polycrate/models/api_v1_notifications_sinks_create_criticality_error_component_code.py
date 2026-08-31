from typing import Literal

ApiV1NotificationsSinksCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_NOTIFICATIONS_SINKS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_notifications_sinks_create_criticality_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksCreateCriticalityErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
