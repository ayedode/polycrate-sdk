from typing import Literal

ApiV1S3ClustersArchiveCreateClusterConfigErrorComponentAttr = Literal["cluster_config"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_CLUSTER_CONFIG_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateClusterConfigErrorComponentAttr
] = {
    "cluster_config",
}


def check_api_v1s3_clusters_archive_create_cluster_config_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateClusterConfigErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_CLUSTER_CONFIG_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_CLUSTER_CONFIG_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
