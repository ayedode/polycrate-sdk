from typing import Literal

ApiV1KubernetesClustersUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_update_archived_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersUpdateArchivedErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
