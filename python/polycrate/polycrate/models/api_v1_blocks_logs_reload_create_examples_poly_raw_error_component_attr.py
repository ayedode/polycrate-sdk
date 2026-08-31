from typing import Literal

ApiV1BlocksLogsReloadCreateExamplesPolyRawErrorComponentAttr = Literal["examples_poly_raw"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateExamplesPolyRawErrorComponentAttr
] = {
    "examples_poly_raw",
}


def check_api_v1_blocks_logs_reload_create_examples_poly_raw_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateExamplesPolyRawErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_EXAMPLES_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
