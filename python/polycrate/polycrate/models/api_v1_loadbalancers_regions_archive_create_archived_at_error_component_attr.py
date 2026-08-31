from typing import Literal

ApiV1LoadbalancersRegionsArchiveCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsArchiveCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_loadbalancers_regions_archive_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsArchiveCreateArchivedAtErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
