from typing import Literal

ApiV1IpaddressesUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_IPADDRESSES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_ipaddresses_update_provider_error_component_attr(
    value: str,
) -> ApiV1IpaddressesUpdateProviderErrorComponentAttr:
    if value in API_V1_IPADDRESSES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
