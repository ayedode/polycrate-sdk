from typing import Literal

ApiV1S3ClustersCreateClusterInfoErrorComponentCode = Literal["invalid"]

API_V1S3_CLUSTERS_CREATE_CLUSTER_INFO_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersCreateClusterInfoErrorComponentCode
] = {
    "invalid",
}


def check_api_v1s3_clusters_create_cluster_info_error_component_code(
    value: str,
) -> ApiV1S3ClustersCreateClusterInfoErrorComponentCode:
    if value in API_V1S3_CLUSTERS_CREATE_CLUSTER_INFO_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_CLUSTER_INFO_ERROR_COMPONENT_CODE_VALUES!r}"
    )
