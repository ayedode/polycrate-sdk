from typing import Literal

PatchedK8SAppRequestScope = Literal["system", "user"]

PATCHED_K8S_APP_REQUEST_SCOPE_VALUES: set[PatchedK8SAppRequestScope] = {
    "system",
    "user",
}


def check_patched_k8s_app_request_scope(value: str) -> PatchedK8SAppRequestScope:
    if value in PATCHED_K8S_APP_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_APP_REQUEST_SCOPE_VALUES!r}")
