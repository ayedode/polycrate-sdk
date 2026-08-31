from typing import Literal

ApiV1BlocksUpdateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_BLOCKS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksUpdateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_blocks_update_created_by_component_error_component_code(
    value: str,
) -> ApiV1BlocksUpdateCreatedByComponentErrorComponentCode:
    if value in API_V1_BLOCKS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
