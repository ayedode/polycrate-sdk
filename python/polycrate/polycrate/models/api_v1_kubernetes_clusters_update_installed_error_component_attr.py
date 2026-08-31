from typing import Literal

ApiV1KubernetesClustersUpdateInstalledErrorComponentAttr = Literal["installed"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersUpdateInstalledErrorComponentAttr
] = {
    "installed",
}


def check_api_v1_kubernetes_clusters_update_installed_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersUpdateInstalledErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
