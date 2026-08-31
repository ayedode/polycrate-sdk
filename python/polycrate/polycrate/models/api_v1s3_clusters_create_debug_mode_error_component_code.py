from typing import Literal

ApiV1S3ClustersCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1S3_CLUSTERS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_clusters_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1S3ClustersCreateDebugModeErrorComponentCode:
    if value in API_V1S3_CLUSTERS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
