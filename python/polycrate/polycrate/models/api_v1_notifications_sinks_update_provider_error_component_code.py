from typing import Literal

ApiV1NotificationsSinksUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotificationsSinksUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_notifications_sinks_update_provider_error_component_code(
    value: str,
) -> ApiV1NotificationsSinksUpdateProviderErrorComponentCode:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
