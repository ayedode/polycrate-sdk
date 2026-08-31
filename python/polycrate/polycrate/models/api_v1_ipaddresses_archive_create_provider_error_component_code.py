from typing import Literal

ApiV1IpaddressesArchiveCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_IPADDRESSES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesArchiveCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_ipaddresses_archive_create_provider_error_component_code(
    value: str,
) -> ApiV1IpaddressesArchiveCreateProviderErrorComponentCode:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
