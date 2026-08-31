from typing import Literal

ApiV1KubernetesWorkerPoolsListSearchErrorComponentAttr = Literal["search"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_kubernetes_worker_pools_list_search_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsListSearchErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
