from typing import Literal

ApiV1KubernetesAppsDiscoverCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_kubernetes_apps_discover_create_annotations_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateAnnotationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
