from typing import Literal

ApiV1IpaddressesUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_IPADDRESSES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_ipaddresses_update_provider_error_component_code(
    value: str,
) -> ApiV1IpaddressesUpdateProviderErrorComponentCode:
    if value in API_V1_IPADDRESSES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
