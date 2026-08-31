from typing import Literal

ApiV1PopsDiscoverCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_POPS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsDiscoverCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pops_discover_create_provider_error_component_attr(
    value: str,
) -> ApiV1PopsDiscoverCreateProviderErrorComponentAttr:
    if value in API_V1_POPS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
