from typing import Literal

ApiV1NotificationsSinksCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_create_tolerations_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksCreateTolerationsErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
