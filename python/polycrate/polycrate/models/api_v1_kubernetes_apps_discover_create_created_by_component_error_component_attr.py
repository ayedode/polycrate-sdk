from typing import Literal

ApiV1KubernetesAppsDiscoverCreateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_kubernetes_apps_discover_create_created_by_component_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateCreatedByComponentErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
