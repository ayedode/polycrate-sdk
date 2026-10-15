from typing import Literal

K8SWorkerPoolListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

K8S_WORKER_POOL_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[K8SWorkerPoolListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_k8s_worker_pool_list_effective_criticality_type_1(value: str) -> K8SWorkerPoolListEffectiveCriticalityType1:
    if value in K8S_WORKER_POOL_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {K8S_WORKER_POOL_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
