from typing import Literal

ApiV1LoadbalancersRegionsCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_LOADBALANCERS_REGIONS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_loadbalancers_regions_create_provider_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateProviderErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
