from typing import Literal

ApiV1NotificationsSinksPartialUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksPartialUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_notifications_sinks_partial_update_annotations_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksPartialUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
