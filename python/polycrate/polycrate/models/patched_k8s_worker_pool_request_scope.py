from typing import Literal

PatchedK8SWorkerPoolRequestScope = Literal["system", "user"]

PATCHED_K8S_WORKER_POOL_REQUEST_SCOPE_VALUES: set[PatchedK8SWorkerPoolRequestScope] = {
    "system",
    "user",
}


def check_patched_k8s_worker_pool_request_scope(value: str) -> PatchedK8SWorkerPoolRequestScope:
    if value in PATCHED_K8S_WORKER_POOL_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_WORKER_POOL_REQUEST_SCOPE_VALUES!r}")
