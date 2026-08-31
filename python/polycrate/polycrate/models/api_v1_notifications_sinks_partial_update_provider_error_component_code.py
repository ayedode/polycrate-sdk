from typing import Literal

ApiV1NotificationsSinksPartialUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksPartialUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_notifications_sinks_partial_update_provider_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksPartialUpdateProviderErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
