from typing import Literal

ApiV1IpaddressesArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_IPADDRESSES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_ipaddresses_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1IpaddressesArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
