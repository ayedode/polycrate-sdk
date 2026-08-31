from typing import Literal

ApiV1KubernetesClustersDiscoverCreateInstalledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_INSTALLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersDiscoverCreateInstalledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_clusters_discover_create_installed_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersDiscoverCreateInstalledErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_INSTALLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_DISCOVER_CREATE_INSTALLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
