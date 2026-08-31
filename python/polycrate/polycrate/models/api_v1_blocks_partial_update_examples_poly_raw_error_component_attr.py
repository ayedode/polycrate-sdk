from typing import Literal

ApiV1BlocksPartialUpdateExamplesPolyRawErrorComponentAttr = Literal["examples_poly_raw"]

API_V1_BLOCKS_PARTIAL_UPDATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateExamplesPolyRawErrorComponentAttr
] = {
    "examples_poly_raw",
}


def check_api_v1_blocks_partial_update_examples_poly_raw_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateExamplesPolyRawErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
