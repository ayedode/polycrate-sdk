from typing import Literal

K8SWorkerPoolRequestScope = Literal["system", "user"]

K8S_WORKER_POOL_REQUEST_SCOPE_VALUES: set[K8SWorkerPoolRequestScope] = {
    "system",
    "user",
}


def check_k8s_worker_pool_request_scope(value: str) -> K8SWorkerPoolRequestScope:
    if value in K8S_WORKER_POOL_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_WORKER_POOL_REQUEST_SCOPE_VALUES!r}")
