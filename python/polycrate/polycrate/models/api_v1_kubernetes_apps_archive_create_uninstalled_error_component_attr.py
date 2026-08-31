from typing import Literal

ApiV1KubernetesAppsArchiveCreateUninstalledErrorComponentAttr = Literal["uninstalled"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateUninstalledErrorComponentAttr
] = {
    "uninstalled",
}


def check_api_v1_kubernetes_apps_archive_create_uninstalled_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateUninstalledErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_UNINSTALLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
