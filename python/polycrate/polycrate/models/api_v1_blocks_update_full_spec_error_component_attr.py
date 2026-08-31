from typing import Literal

ApiV1BlocksUpdateFullSpecErrorComponentAttr = Literal["full_spec"]

API_V1_BLOCKS_UPDATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksUpdateFullSpecErrorComponentAttr] = {
    "full_spec",
}


def check_api_v1_blocks_update_full_spec_error_component_attr(
    value: str,
) -> ApiV1BlocksUpdateFullSpecErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
