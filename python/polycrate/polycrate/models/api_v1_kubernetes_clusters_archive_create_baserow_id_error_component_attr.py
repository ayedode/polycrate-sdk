from typing import Literal

ApiV1KubernetesClustersArchiveCreateBaserowIdErrorComponentAttr = Literal["baserow_id"]

API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_BASEROW_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersArchiveCreateBaserowIdErrorComponentAttr
] = {
    "baserow_id",
}


def check_api_v1_kubernetes_clusters_archive_create_baserow_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersArchiveCreateBaserowIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_BASEROW_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_BASEROW_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
