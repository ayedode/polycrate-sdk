from typing import Literal

ApiV1KubernetesAppsUninstallCreateNamespaceErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateNamespaceErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_apps_uninstall_create_namespace_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateNamespaceErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
