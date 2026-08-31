from typing import Literal

ApiV1NotificationsSinksUpdateKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1_notifications_sinks_update_kind_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksUpdateKindErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
