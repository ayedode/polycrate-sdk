from typing import Literal

ApiV1BlocksCheckCreateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_BLOCKS_CHECK_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksCheckCreateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_blocks_check_create_created_by_component_error_component_code(
    value: str,
) -> ApiV1BlocksCheckCreateCreatedByComponentErrorComponentCode:
    if value in API_V1_BLOCKS_CHECK_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
