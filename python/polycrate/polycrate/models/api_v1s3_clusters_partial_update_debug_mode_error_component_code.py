from typing import Literal

ApiV1S3ClustersPartialUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersPartialUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_clusters_partial_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1S3ClustersPartialUpdateDebugModeErrorComponentCode:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
