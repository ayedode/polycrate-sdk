from typing import Literal

ApiV1IpaddressesArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_IPADDRESSES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_ipaddresses_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1IpaddressesArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
