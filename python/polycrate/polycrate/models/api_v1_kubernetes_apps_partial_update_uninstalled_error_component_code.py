from typing import Literal

ApiV1KubernetesAppsPartialUpdateUninstalledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateUninstalledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_partial_update_uninstalled_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateUninstalledErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
