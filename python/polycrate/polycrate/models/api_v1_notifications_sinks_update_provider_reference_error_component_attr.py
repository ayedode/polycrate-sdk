from typing import Literal

ApiV1NotificationsSinksUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_NOTIFICATIONS_SINKS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_notifications_sinks_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
