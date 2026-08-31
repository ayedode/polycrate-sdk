from typing import Literal

ApiV1KubernetesWorkerPoolsListScope = Literal["system", "user"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_SCOPE_VALUES: set[ApiV1KubernetesWorkerPoolsListScope] = {
    "system",
    "user",
}


def check_api_v1_kubernetes_worker_pools_list_scope(value: str) -> ApiV1KubernetesWorkerPoolsListScope:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_SCOPE_VALUES!r}")
