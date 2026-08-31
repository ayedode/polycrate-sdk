from typing import Literal

ApiV1IpaddressesArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_IPADDRESSES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_ipaddresses_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1IpaddressesArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
