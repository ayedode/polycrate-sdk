from typing import Literal

K8SControlplaneCriticalityType1 = Literal["", "high", "low", "medium"]

K8S_CONTROLPLANE_CRITICALITY_TYPE_1_VALUES: set[K8SControlplaneCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_k8s_controlplane_criticality_type_1(value: str) -> K8SControlplaneCriticalityType1:
    if value in K8S_CONTROLPLANE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_CONTROLPLANE_CRITICALITY_TYPE_1_VALUES!r}")
