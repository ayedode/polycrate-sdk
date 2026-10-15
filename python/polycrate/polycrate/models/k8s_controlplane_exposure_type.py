from typing import Literal

K8SControlplaneExposureType = Literal["gateway", "ingress", "loadbalancer"]

K8S_CONTROLPLANE_EXPOSURE_TYPE_VALUES: set[K8SControlplaneExposureType] = {
    "gateway",
    "ingress",
    "loadbalancer",
}


def check_k8s_controlplane_exposure_type(value: str) -> K8SControlplaneExposureType:
    if value in K8S_CONTROLPLANE_EXPOSURE_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CONTROLPLANE_EXPOSURE_TYPE_VALUES!r}")
