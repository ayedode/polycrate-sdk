from typing import Literal

ApiV1BlocksPartialUpdateFullSpecErrorComponentAttr = Literal["full_spec"]

API_V1_BLOCKS_PARTIAL_UPDATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateFullSpecErrorComponentAttr
] = {
    "full_spec",
}


def check_api_v1_blocks_partial_update_full_spec_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateFullSpecErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
