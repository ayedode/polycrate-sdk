from typing import Literal

ApiV1KubernetesAppsDiscoverCreateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1_kubernetes_apps_discover_create_namespace_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateNamespaceErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
