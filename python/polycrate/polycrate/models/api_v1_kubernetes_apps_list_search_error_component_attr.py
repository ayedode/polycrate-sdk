from typing import Literal

ApiV1KubernetesAppsListSearchErrorComponentAttr = Literal["search"]

API_V1_KUBERNETES_APPS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1KubernetesAppsListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_kubernetes_apps_list_search_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsListSearchErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
