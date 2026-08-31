from typing import Literal

ApiV1BlocksDiscoverCreateFullSpecErrorComponentAttr = Literal["full_spec"]

API_V1_BLOCKS_DISCOVER_CREATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateFullSpecErrorComponentAttr
] = {
    "full_spec",
}


def check_api_v1_blocks_discover_create_full_spec_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateFullSpecErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
