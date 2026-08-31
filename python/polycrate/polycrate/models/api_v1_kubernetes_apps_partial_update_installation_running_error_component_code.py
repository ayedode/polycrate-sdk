from typing import Literal

ApiV1KubernetesAppsPartialUpdateInstallationRunningErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_INSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateInstallationRunningErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_partial_update_installation_running_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateInstallationRunningErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_INSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_INSTALLATION_RUNNING_ERROR_COMPONENT_CODE_VALUES!r}"
    )
