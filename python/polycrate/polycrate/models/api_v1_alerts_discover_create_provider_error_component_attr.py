from typing import Literal

ApiV1AlertsDiscoverCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ALERTS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_alerts_discover_create_provider_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateProviderErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
