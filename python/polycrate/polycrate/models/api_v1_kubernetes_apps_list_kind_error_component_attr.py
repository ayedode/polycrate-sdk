from typing import Literal

ApiV1KubernetesAppsListKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_APPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1KubernetesAppsListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_kubernetes_apps_list_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsListKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
