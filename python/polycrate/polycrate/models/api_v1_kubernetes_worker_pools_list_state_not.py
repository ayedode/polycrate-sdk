from typing import Literal

ApiV1KubernetesWorkerPoolsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_STATE_NOT_VALUES: set[ApiV1KubernetesWorkerPoolsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_kubernetes_worker_pools_list_state_not(value: str) -> ApiV1KubernetesWorkerPoolsListStateNot:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_STATE_NOT_VALUES!r}"
    )
