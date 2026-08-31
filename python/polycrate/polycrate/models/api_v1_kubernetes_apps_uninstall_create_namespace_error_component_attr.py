from typing import Literal

ApiV1KubernetesAppsUninstallCreateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1_kubernetes_apps_uninstall_create_namespace_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateNamespaceErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
