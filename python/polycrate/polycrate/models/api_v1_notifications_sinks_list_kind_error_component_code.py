from typing import Literal

ApiV1NotificationsSinksListKindErrorComponentCode = Literal["invalid_choice"]

API_V1_NOTIFICATIONS_SINKS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksListKindErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_notifications_sinks_list_kind_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksListKindErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
