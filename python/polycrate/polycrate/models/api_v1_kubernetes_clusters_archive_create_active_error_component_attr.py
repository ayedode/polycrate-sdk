from typing import Literal

ApiV1KubernetesClustersArchiveCreateActiveErrorComponentAttr = Literal["active"]

API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersArchiveCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_kubernetes_clusters_archive_create_active_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersArchiveCreateActiveErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
