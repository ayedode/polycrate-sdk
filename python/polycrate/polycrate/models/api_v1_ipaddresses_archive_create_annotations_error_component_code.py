from typing import Literal

ApiV1IpaddressesArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_IPADDRESSES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_ipaddresses_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1IpaddressesArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
