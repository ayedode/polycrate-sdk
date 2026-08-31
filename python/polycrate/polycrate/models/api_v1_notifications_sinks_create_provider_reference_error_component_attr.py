from typing import Literal

ApiV1NotificationsSinksCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_NOTIFICATIONS_SINKS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotificationsSinksCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_notifications_sinks_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1NotificationsSinksCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_NOTIFICATIONS_SINKS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTIFICATIONS_SINKS_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
