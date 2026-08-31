from typing import Literal

ApiV1LoadbalancersRegionsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_LOADBALANCERS_REGIONS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_loadbalancers_regions_create_provider_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateProviderErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
