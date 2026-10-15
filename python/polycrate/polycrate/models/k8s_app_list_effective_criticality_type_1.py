from typing import Literal

K8SAppListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

K8S_APP_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[K8SAppListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_k8s_app_list_effective_criticality_type_1(value: str) -> K8SAppListEffectiveCriticalityType1:
    if value in K8S_APP_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_APP_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
