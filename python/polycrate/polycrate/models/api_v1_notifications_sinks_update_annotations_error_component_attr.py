from typing import Literal

ApiV1NotificationsSinksUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_notifications_sinks_update_annotations_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
