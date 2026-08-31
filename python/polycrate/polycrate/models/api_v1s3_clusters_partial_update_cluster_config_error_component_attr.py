from typing import Literal

ApiV1S3ClustersPartialUpdateClusterConfigErrorComponentAttr = Literal["cluster_config"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_CLUSTER_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateClusterConfigErrorComponentAttr
] = {
    "cluster_config",
}


def check_api_v1s3_clusters_partial_update_cluster_config_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateClusterConfigErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_CLUSTER_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_CLUSTER_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
