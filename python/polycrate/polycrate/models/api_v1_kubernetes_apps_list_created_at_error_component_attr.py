from typing import Literal

ApiV1KubernetesAppsListCreatedAtErrorComponentAttr = Literal["created_at"]

API_V1_KUBERNETES_APPS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsListCreatedAtErrorComponentAttr
] = {
    "created_at",
}


def check_api_v1_kubernetes_apps_list_created_at_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsListCreatedAtErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
