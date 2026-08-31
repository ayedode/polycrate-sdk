from typing import Literal

ApiV1KubernetesClustersPartialUpdateInstalledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_INSTALLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateInstalledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_partial_update_installed_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateInstalledErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_INSTALLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_INSTALLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
