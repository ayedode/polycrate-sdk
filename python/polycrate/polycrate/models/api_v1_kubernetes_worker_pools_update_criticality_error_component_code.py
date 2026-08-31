from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_worker_pools_update_criticality_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateCriticalityErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
