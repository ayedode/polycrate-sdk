from typing import Literal

K8SWorkerPoolScope = Literal["system", "user"]

K8S_WORKER_POOL_SCOPE_VALUES: set[K8SWorkerPoolScope] = {
    "system",
    "user",
}


def check_k8s_worker_pool_scope(value: str) -> K8SWorkerPoolScope:
    if value in K8S_WORKER_POOL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_WORKER_POOL_SCOPE_VALUES!r}")
