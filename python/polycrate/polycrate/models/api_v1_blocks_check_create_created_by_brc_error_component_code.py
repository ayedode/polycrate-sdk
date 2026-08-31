from typing import Literal

ApiV1BlocksCheckCreateCreatedByBrcErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_BLOCKS_CHECK_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksCheckCreateCreatedByBrcErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_blocks_check_create_created_by_brc_error_component_code(
    value: str,
) -> ApiV1BlocksCheckCreateCreatedByBrcErrorComponentCode:
    if value in API_V1_BLOCKS_CHECK_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_CODE_VALUES!r}"
    )
