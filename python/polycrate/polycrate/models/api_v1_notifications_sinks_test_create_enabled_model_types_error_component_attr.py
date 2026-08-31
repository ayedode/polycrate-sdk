from typing import Literal

ApiV1NotificationsSinksTestCreateEnabledModelTypesErrorComponentAttr = Literal["enabled_model_types"]

API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ENABLED_MODEL_TYPES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksTestCreateEnabledModelTypesErrorComponentAttr
] = {
    "enabled_model_types",
}


def check_api_v1_notifications_sinks_test_create_enabled_model_types_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksTestCreateEnabledModelTypesErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ENABLED_MODEL_TYPES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_TEST_CREATE_ENABLED_MODEL_TYPES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
