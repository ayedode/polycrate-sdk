from typing import Literal

ApiV1KubernetesWorkerPoolsListKindItem = Literal["generic"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_KIND_ITEM_VALUES: set[ApiV1KubernetesWorkerPoolsListKindItem] = {
    "generic",
}


def check_api_v1_kubernetes_worker_pools_list_kind_item(value: str) -> ApiV1KubernetesWorkerPoolsListKindItem:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_KIND_ITEM_VALUES!r}"
    )
