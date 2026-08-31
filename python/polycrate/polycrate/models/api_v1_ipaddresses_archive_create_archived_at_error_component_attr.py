from typing import Literal

ApiV1IpaddressesArchiveCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_IPADDRESSES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesArchiveCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_ipaddresses_archive_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1IpaddressesArchiveCreateArchivedAtErrorComponentAttr:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
