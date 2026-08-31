from typing import Literal

ApiV1S3ClustersArchiveCreateK8SClusterErrorComponentCode = Literal["does_not_exist", "incorrect_type", "required"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersArchiveCreateK8SClusterErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "required",
}


def check_api_v1s3_clusters_archive_create_k8s_cluster_error_component_code(
    value: str,
) -> ApiV1S3ClustersArchiveCreateK8SClusterErrorComponentCode:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_K8S_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
