from typing import Literal

ApiV1S3ClustersUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1S3_CLUSTERS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1s3_clusters_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateDebugModeErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
