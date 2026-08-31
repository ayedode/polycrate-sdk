from typing import Literal

ApiV1KubernetesWorkerPoolsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_STATE_VALUES: set[ApiV1KubernetesWorkerPoolsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_kubernetes_worker_pools_list_state(value: str) -> ApiV1KubernetesWorkerPoolsListState:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_STATE_VALUES!r}")
