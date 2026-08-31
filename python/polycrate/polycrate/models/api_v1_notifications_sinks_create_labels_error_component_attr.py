from typing import Literal

ApiV1NotificationsSinksCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_NOTIFICATIONS_SINKS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_notifications_sinks_create_labels_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksCreateLabelsErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
