from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedK8SClusterCountErrorComponentAttr = Literal["cached_k8s_cluster_count"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_K8S_CLUSTER_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedK8SClusterCountErrorComponentAttr
] = {
    "cached_k8s_cluster_count",
}


def check_api_v1_organizations_icon_upload_create_cached_k8s_cluster_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedK8SClusterCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_K8S_CLUSTER_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_K8S_CLUSTER_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
