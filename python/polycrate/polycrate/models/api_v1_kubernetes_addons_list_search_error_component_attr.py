from typing import Literal

ApiV1KubernetesAddonsListSearchErrorComponentAttr = Literal["search"]

API_V1_KUBERNETES_ADDONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_kubernetes_addons_list_search_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsListSearchErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
