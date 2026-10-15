from typing import Literal

K8SWorkerPoolLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

K8S_WORKER_POOL_LAST_STATE_VALUES: set[K8SWorkerPoolLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_k8s_worker_pool_last_state(value: str) -> K8SWorkerPoolLastState:
    if value in K8S_WORKER_POOL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_WORKER_POOL_LAST_STATE_VALUES!r}")
