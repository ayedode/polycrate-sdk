from typing import Literal

ApiV1NotificationsSinksCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_NOTIFICATIONS_SINKS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_notifications_sinks_create_labels_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksCreateLabelsErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
