from typing import Literal

ApiV1EndpointsDiscoverCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ENDPOINTS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_endpoints_discover_create_provider_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateProviderErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
