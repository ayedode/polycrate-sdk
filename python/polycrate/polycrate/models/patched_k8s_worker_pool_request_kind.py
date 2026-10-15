from typing import Literal

PatchedK8SWorkerPoolRequestKind = Literal["generic"]

PATCHED_K8S_WORKER_POOL_REQUEST_KIND_VALUES: set[PatchedK8SWorkerPoolRequestKind] = {
    "generic",
}


def check_patched_k8s_worker_pool_request_kind(value: str) -> PatchedK8SWorkerPoolRequestKind:
    if value in PATCHED_K8S_WORKER_POOL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_WORKER_POOL_REQUEST_KIND_VALUES!r}")
