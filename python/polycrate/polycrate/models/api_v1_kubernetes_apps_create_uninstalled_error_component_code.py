from typing import Literal

ApiV1KubernetesAppsCreateUninstalledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_CREATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsCreateUninstalledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_create_uninstalled_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsCreateUninstalledErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_CREATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_UNINSTALLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
