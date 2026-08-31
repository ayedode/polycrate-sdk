from typing import Literal

ApiV1BlocksDiscoverCreateKindErrorComponentAttr = Literal["kind"]

API_V1_BLOCKS_DISCOVER_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksDiscoverCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_blocks_discover_create_kind_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateKindErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
