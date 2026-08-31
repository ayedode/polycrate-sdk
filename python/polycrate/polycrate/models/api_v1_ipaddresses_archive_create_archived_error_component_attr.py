from typing import Literal

ApiV1IpaddressesArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_IPADDRESSES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_ipaddresses_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1IpaddressesArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_IPADDRESSES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
