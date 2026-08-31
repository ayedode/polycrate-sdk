from typing import Literal

ApiV1BlocksCreateExamplesPolyRawErrorComponentAttr = Literal["examples_poly_raw"]

API_V1_BLOCKS_CREATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCreateExamplesPolyRawErrorComponentAttr
] = {
    "examples_poly_raw",
}


def check_api_v1_blocks_create_examples_poly_raw_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateExamplesPolyRawErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
