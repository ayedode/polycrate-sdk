from typing import Literal

PatchedK8SVolumeRequestKind = Literal["generic"]

PATCHED_K8S_VOLUME_REQUEST_KIND_VALUES: set[PatchedK8SVolumeRequestKind] = {
    "generic",
}


def check_patched_k8s_volume_request_kind(value: str) -> PatchedK8SVolumeRequestKind:
    if value in PATCHED_K8S_VOLUME_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_VOLUME_REQUEST_KIND_VALUES!r}")
