from typing import Literal

ApiV1NotificationsSinksListUpdatedAtErrorComponentCode = Literal["invalid"]

API_V1_NOTIFICATIONS_SINKS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksListUpdatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_notifications_sinks_list_updated_at_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksListUpdatedAtErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
