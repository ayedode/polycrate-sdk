from typing import Literal

ApiV1KubernetesWorkerPoolsCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_worker_pools_create_criticality_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateCriticalityErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
