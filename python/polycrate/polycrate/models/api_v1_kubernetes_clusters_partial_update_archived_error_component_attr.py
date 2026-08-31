from typing import Literal

ApiV1KubernetesClustersPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_clusters_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
