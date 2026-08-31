from typing import Literal

ApiV1KubernetesAppsDiscoverCreateBlockErrorComponentAttr = Literal["block"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateBlockErrorComponentAttr
] = {
    "block",
}


def check_api_v1_kubernetes_apps_discover_create_block_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateBlockErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
