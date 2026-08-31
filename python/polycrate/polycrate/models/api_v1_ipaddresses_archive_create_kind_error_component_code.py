from typing import Literal

ApiV1IpaddressesArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_IPADDRESSES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_ipaddresses_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1IpaddressesArchiveCreateKindErrorComponentCode:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
