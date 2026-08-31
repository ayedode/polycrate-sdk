from typing import Literal

ApiV1KubernetesAppsCreateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_KUBERNETES_APPS_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1_kubernetes_apps_create_namespace_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateNamespaceErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
