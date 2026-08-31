from typing import Literal

ApiV1BlocksPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCKS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksPartialUpdateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_blocks_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1BlocksPartialUpdateKindErrorComponentCode:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
