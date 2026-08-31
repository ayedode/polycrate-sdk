from typing import Literal

ApiV1KubernetesAppsArchiveCreateLastInstallationErrorComponentAttr = Literal["last_installation"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateLastInstallationErrorComponentAttr
] = {
    "last_installation",
}


def check_api_v1_kubernetes_apps_archive_create_last_installation_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateLastInstallationErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
