from typing import Literal

K8SWorkerPoolRequestKind = Literal["generic"]

K8S_WORKER_POOL_REQUEST_KIND_VALUES: set[K8SWorkerPoolRequestKind] = {
    "generic",
}


def check_k8s_worker_pool_request_kind(value: str) -> K8SWorkerPoolRequestKind:
    if value in K8S_WORKER_POOL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_WORKER_POOL_REQUEST_KIND_VALUES!r}")
