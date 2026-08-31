from typing import Literal

ApiV1NotificationsSinksUpdateEnabledModelTypesErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_ENABLED_MODEL_TYPES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksUpdateEnabledModelTypesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notifications_sinks_update_enabled_model_types_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksUpdateEnabledModelTypesErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_ENABLED_MODEL_TYPES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_ENABLED_MODEL_TYPES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
