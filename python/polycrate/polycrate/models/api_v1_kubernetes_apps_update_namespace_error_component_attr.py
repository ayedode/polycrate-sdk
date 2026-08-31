from typing import Literal

ApiV1KubernetesAppsUpdateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_KUBERNETES_APPS_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1_kubernetes_apps_update_namespace_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateNamespaceErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
