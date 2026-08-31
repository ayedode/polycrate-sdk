from typing import Literal

ApiV1NotificationsSinksTestCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksTestCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_notifications_sinks_test_create_criticality_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksTestCreateCriticalityErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
