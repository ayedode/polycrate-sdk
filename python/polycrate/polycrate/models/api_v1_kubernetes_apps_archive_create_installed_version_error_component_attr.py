from typing import Literal

ApiV1KubernetesAppsArchiveCreateInstalledVersionErrorComponentAttr = Literal["installed_version"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_INSTALLED_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateInstalledVersionErrorComponentAttr
] = {
    "installed_version",
}


def check_api_v1_kubernetes_apps_archive_create_installed_version_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateInstalledVersionErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_INSTALLED_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_INSTALLED_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
