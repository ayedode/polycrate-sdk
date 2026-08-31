from typing import Literal

ApiV1BlocksDiscoverCreateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_BLOCKS_DISCOVER_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksDiscoverCreateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_blocks_discover_create_archived_at_error_component_code(
    value: str,
) -> ApiV1BlocksDiscoverCreateArchivedAtErrorComponentCode:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
