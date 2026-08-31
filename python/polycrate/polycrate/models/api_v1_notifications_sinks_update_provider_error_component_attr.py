from typing import Literal

ApiV1NotificationsSinksUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_notifications_sinks_update_provider_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksUpdateProviderErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
