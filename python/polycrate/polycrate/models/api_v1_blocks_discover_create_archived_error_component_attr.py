from typing import Literal

ApiV1BlocksDiscoverCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_BLOCKS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_blocks_discover_create_archived_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateArchivedErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
