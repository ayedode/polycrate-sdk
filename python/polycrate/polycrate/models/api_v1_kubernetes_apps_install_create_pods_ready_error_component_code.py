from typing import Literal

ApiV1KubernetesAppsInstallCreatePodsReadyErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_PODS_READY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsInstallCreatePodsReadyErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_kubernetes_apps_install_create_pods_ready_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsInstallCreatePodsReadyErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_PODS_READY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_PODS_READY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
