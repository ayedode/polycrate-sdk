from typing import Literal

ApiV1PopsDiscoverCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_POPS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PopsDiscoverCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pops_discover_create_provider_error_component_code(
    value: str,
) -> ApiV1PopsDiscoverCreateProviderErrorComponentCode:
    if value in API_V1_POPS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
