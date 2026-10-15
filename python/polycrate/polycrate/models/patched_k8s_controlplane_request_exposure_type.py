from typing import Literal

PatchedK8SControlplaneRequestExposureType = Literal["gateway", "ingress", "loadbalancer"]

PATCHED_K8S_CONTROLPLANE_REQUEST_EXPOSURE_TYPE_VALUES: set[PatchedK8SControlplaneRequestExposureType] = {
    "gateway",
    "ingress",
    "loadbalancer",
}


def check_patched_k8s_controlplane_request_exposure_type(value: str) -> PatchedK8SControlplaneRequestExposureType:
    if value in PATCHED_K8S_CONTROLPLANE_REQUEST_EXPOSURE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_CONTROLPLANE_REQUEST_EXPOSURE_TYPE_VALUES!r}"
    )
