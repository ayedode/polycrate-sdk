from typing import Literal

ApiV1KubernetesAppsInstallCreateInstallationRunningErrorComponentAttr = Literal["installation_running"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateInstallationRunningErrorComponentAttr
] = {
    "installation_running",
}


def check_api_v1_kubernetes_apps_install_create_installation_running_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateInstallationRunningErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
