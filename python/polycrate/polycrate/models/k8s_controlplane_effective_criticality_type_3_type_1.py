from typing import Literal

K8SControlplaneEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

K8S_CONTROLPLANE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[K8SControlplaneEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_k8s_controlplane_effective_criticality_type_3_type_1(
    value: str,
) -> K8SControlplaneEffectiveCriticalityType3Type1:
    if value in K8S_CONTROLPLANE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_CONTROLPLANE_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
