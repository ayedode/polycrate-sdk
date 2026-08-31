from typing import Literal

ApiV1KubernetesAppsCreateInstallationRunningErrorComponentAttr = Literal["installation_running"]

API_V1_KUBERNETES_APPS_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateInstallationRunningErrorComponentAttr
] = {
    "installation_running",
}


def check_api_v1_kubernetes_apps_create_installation_running_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateInstallationRunningErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
