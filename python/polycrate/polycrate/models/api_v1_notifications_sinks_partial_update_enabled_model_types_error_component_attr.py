from typing import Literal

ApiV1NotificationsSinksPartialUpdateEnabledModelTypesErrorComponentAttr = Literal["enabled_model_types"]

API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_ENABLED_MODEL_TYPES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksPartialUpdateEnabledModelTypesErrorComponentAttr
] = {
    "enabled_model_types",
}


def check_api_v1_notifications_sinks_partial_update_enabled_model_types_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksPartialUpdateEnabledModelTypesErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_ENABLED_MODEL_TYPES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_ENABLED_MODEL_TYPES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
