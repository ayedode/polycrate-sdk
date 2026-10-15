from typing import Literal

K8SControlplaneRequestExposureType = Literal["gateway", "ingress", "loadbalancer"]

K8S_CONTROLPLANE_REQUEST_EXPOSURE_TYPE_VALUES: set[K8SControlplaneRequestExposureType] = {
    "gateway",
    "ingress",
    "loadbalancer",
}


def check_k8s_controlplane_request_exposure_type(value: str) -> K8SControlplaneRequestExposureType:
    if value in K8S_CONTROLPLANE_REQUEST_EXPOSURE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CONTROLPLANE_REQUEST_EXPOSURE_TYPE_VALUES!r}")
