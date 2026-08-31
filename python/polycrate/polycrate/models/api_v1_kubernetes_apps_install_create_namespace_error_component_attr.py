from typing import Literal

ApiV1KubernetesAppsInstallCreateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1_kubernetes_apps_install_create_namespace_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateNamespaceErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
