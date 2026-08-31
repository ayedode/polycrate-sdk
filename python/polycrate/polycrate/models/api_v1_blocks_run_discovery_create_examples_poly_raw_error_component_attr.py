from typing import Literal

ApiV1BlocksRunDiscoveryCreateExamplesPolyRawErrorComponentAttr = Literal["examples_poly_raw"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateExamplesPolyRawErrorComponentAttr
] = {
    "examples_poly_raw",
}


def check_api_v1_blocks_run_discovery_create_examples_poly_raw_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateExamplesPolyRawErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
