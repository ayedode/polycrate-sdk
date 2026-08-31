from typing import Literal

ApiV1S3ClustersPartialUpdateClusterConfigErrorComponentCode = Literal["invalid", "null"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_CLUSTER_CONFIG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersPartialUpdateClusterConfigErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_clusters_partial_update_cluster_config_error_component_code(
    value: str,
) -> ApiV1S3ClustersPartialUpdateClusterConfigErrorComponentCode:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_CLUSTER_CONFIG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_CLUSTER_CONFIG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
