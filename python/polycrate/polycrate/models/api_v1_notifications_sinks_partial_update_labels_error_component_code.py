from typing import Literal

ApiV1NotificationsSinksPartialUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksPartialUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_notifications_sinks_partial_update_labels_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksPartialUpdateLabelsErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
