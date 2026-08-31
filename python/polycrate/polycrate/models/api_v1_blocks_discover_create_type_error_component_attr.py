from typing import Literal

ApiV1BlocksDiscoverCreateTypeErrorComponentAttr = Literal["type"]

API_V1_BLOCKS_DISCOVER_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksDiscoverCreateTypeErrorComponentAttr] = {
    "type",
}


def check_api_v1_blocks_discover_create_type_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateTypeErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
