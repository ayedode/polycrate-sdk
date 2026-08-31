from typing import Literal

ApiV1KubernetesAppsDiscoverCreateActiveErrorComponentAttr = Literal["active"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_kubernetes_apps_discover_create_active_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateActiveErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
