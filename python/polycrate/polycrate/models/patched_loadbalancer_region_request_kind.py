from typing import Literal

PatchedLoadbalancerRegionRequestKind = Literal["cilium", "metallb"]

PATCHED_LOADBALANCER_REGION_REQUEST_KIND_VALUES: set[PatchedLoadbalancerRegionRequestKind] = {
    "cilium",
    "metallb",
}


def check_patched_loadbalancer_region_request_kind(value: str) -> PatchedLoadbalancerRegionRequestKind:
    if value in PATCHED_LOADBALANCER_REGION_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_LOADBALANCER_REGION_REQUEST_KIND_VALUES!r}")
