from typing import Literal

K8SWorkerPoolKind = Literal["generic"]

K8S_WORKER_POOL_KIND_VALUES: set[K8SWorkerPoolKind] = {
    "generic",
}


def check_k8s_worker_pool_kind(value: str) -> K8SWorkerPoolKind:
    if value in K8S_WORKER_POOL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_WORKER_POOL_KIND_VALUES!r}")
