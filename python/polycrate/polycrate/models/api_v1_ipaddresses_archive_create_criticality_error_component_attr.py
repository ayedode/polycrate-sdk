from typing import Literal

ApiV1IpaddressesArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_IPADDRESSES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_ipaddresses_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1IpaddressesArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
