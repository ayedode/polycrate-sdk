from typing import Literal

ApiV1KubernetesAppsDiscoverCreateSourceErrorComponentAttr = Literal["source"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateSourceErrorComponentAttr
] = {
    "source",
}


def check_api_v1_kubernetes_apps_discover_create_source_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateSourceErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
