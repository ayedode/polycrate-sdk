from typing import Literal

K8SAppEffectiveCriticalityType1 = Literal["high", "low", "medium"]

K8S_APP_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[K8SAppEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_k8s_app_effective_criticality_type_1(value: str) -> K8SAppEffectiveCriticalityType1:
    if value in K8S_APP_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_APP_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
