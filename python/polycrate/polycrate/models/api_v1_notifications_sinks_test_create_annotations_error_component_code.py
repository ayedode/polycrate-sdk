from typing import Literal

ApiV1NotificationsSinksTestCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksTestCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_notifications_sinks_test_create_annotations_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksTestCreateAnnotationsErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
