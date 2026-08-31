from typing import Literal

ApiV1KubernetesClustersArchiveCreateInstalledErrorComponentAttr = Literal["installed"]

API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersArchiveCreateInstalledErrorComponentAttr
] = {
    "installed",
}


def check_api_v1_kubernetes_clusters_archive_create_installed_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersArchiveCreateInstalledErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_INSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
