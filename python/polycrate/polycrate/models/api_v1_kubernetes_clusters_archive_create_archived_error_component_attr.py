from typing import Literal

ApiV1KubernetesClustersArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_clusters_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
