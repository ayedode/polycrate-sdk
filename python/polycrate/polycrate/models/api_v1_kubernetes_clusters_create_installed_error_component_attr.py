from typing import Literal

ApiV1KubernetesClustersCreateInstalledErrorComponentAttr = Literal["installed"]

API_V1_KUBERNETES_CLUSTERS_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersCreateInstalledErrorComponentAttr
] = {
    "installed",
}


def check_api_v1_kubernetes_clusters_create_installed_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersCreateInstalledErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
