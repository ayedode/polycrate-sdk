from typing import Literal

ApiV1S3ClustersCreateClusterConfigErrorComponentAttr = Literal["cluster_config"]

API_V1S3_CLUSTERS_CREATE_CLUSTER_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateClusterConfigErrorComponentAttr
] = {
    "cluster_config",
}


def check_api_v1s3_clusters_create_cluster_config_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateClusterConfigErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_CLUSTER_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_CLUSTER_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
