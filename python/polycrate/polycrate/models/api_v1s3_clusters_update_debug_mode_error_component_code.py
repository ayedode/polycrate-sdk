from typing import Literal

ApiV1S3ClustersUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1S3_CLUSTERS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_clusters_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1S3ClustersUpdateDebugModeErrorComponentCode:
    if value in API_V1S3_CLUSTERS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
