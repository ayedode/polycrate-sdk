from typing import Literal

ApiV1NotificationsSinksArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_notifications_sinks_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
