from typing import Literal

ApiV1BlocksUpdateExamplesPolyRawErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCKS_UPDATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksUpdateExamplesPolyRawErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_blocks_update_examples_poly_raw_error_component_code(
    value: str,
) -> ApiV1BlocksUpdateExamplesPolyRawErrorComponentCode:
    if value in API_V1_BLOCKS_UPDATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_CODE_VALUES!r}"
    )
