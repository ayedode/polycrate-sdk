from typing import Literal

ApiV1S3ClustersCreateClusterInfoErrorComponentAttr = Literal["cluster_info"]

API_V1S3_CLUSTERS_CREATE_CLUSTER_INFO_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateClusterInfoErrorComponentAttr
] = {
    "cluster_info",
}


def check_api_v1s3_clusters_create_cluster_info_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateClusterInfoErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_CLUSTER_INFO_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_CLUSTER_INFO_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
