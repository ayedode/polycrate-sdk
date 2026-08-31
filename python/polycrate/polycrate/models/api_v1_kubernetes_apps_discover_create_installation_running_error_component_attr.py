from typing import Literal

ApiV1KubernetesAppsDiscoverCreateInstallationRunningErrorComponentAttr = Literal["installation_running"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateInstallationRunningErrorComponentAttr
] = {
    "installation_running",
}


def check_api_v1_kubernetes_apps_discover_create_installation_running_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateInstallationRunningErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_INSTALLATION_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
