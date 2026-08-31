from typing import Literal

ApiV1S3ClustersUpdateK8SClusterErrorComponentCode = Literal["does_not_exist", "incorrect_type", "required"]

API_V1S3_CLUSTERS_UPDATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersUpdateK8SClusterErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "required",
}


def check_api_v1s3_clusters_update_k8s_cluster_error_component_code(
    value: str,
) -> ApiV1S3ClustersUpdateK8SClusterErrorComponentCode:
    if value in API_V1S3_CLUSTERS_UPDATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
