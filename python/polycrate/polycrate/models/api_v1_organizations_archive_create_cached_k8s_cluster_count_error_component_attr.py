from typing import Literal

ApiV1OrganizationsArchiveCreateCachedK8SClusterCountErrorComponentAttr = Literal["cached_k8s_cluster_count"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_K8S_CLUSTER_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateCachedK8SClusterCountErrorComponentAttr
] = {
    "cached_k8s_cluster_count",
}


def check_api_v1_organizations_archive_create_cached_k8s_cluster_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateCachedK8SClusterCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_K8S_CLUSTER_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_CACHED_K8S_CLUSTER_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
