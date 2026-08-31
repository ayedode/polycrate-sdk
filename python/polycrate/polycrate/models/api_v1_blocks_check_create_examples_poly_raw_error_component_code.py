from typing import Literal

ApiV1BlocksCheckCreateExamplesPolyRawErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_CHECK_CREATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksCheckCreateExamplesPolyRawErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_check_create_examples_poly_raw_error_component_code(
    value: str,
) -> ApiV1BlocksCheckCreateExamplesPolyRawErrorComponentCode:
    if value in API_V1_BLOCKS_CHECK_CREATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
