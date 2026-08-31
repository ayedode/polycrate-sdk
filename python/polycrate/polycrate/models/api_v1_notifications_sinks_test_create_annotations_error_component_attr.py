from typing import Literal

ApiV1NotificationsSinksTestCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksTestCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_notifications_sinks_test_create_annotations_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksTestCreateAnnotationsErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
