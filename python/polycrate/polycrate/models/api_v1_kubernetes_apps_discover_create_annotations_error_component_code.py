from typing import Literal

ApiV1KubernetesAppsDiscoverCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_apps_discover_create_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
