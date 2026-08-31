from typing import Literal

ApiV1KubernetesAppsInstallCreatePodsStatusHashErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_PODS_STATUS_HASH_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsInstallCreatePodsStatusHashErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_apps_install_create_pods_status_hash_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsInstallCreatePodsStatusHashErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_PODS_STATUS_HASH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_PODS_STATUS_HASH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
