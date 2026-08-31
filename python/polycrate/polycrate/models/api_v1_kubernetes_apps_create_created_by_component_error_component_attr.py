from typing import Literal

ApiV1KubernetesAppsCreateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_KUBERNETES_APPS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_kubernetes_apps_create_created_by_component_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateCreatedByComponentErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
