from typing import Literal

ApiV1KubernetesAppsUninstallCreateLastInstallationErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateLastInstallationErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_kubernetes_apps_uninstall_create_last_installation_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateLastInstallationErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_LAST_INSTALLATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
