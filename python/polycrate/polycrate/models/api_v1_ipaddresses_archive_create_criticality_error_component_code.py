from typing import Literal

ApiV1IpaddressesArchiveCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_IPADDRESSES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesArchiveCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_ipaddresses_archive_create_criticality_error_component_code(
    value: str,
) -> ApiV1IpaddressesArchiveCreateCriticalityErrorComponentCode:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
