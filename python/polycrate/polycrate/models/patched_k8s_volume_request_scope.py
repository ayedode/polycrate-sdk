from typing import Literal

PatchedK8SVolumeRequestScope = Literal["system", "user"]

PATCHED_K8S_VOLUME_REQUEST_SCOPE_VALUES: set[PatchedK8SVolumeRequestScope] = {
    "system",
    "user",
}


def check_patched_k8s_volume_request_scope(value: str) -> PatchedK8SVolumeRequestScope:
    if value in PATCHED_K8S_VOLUME_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_VOLUME_REQUEST_SCOPE_VALUES!r}")
