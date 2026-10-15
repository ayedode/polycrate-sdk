from typing import Literal

K8SWorkerPoolState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_WORKER_POOL_STATE_VALUES: set[K8SWorkerPoolState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_worker_pool_state(value: str) -> K8SWorkerPoolState:
    if value in K8S_WORKER_POOL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_WORKER_POOL_STATE_VALUES!r}")
