from typing import Literal

ApiV1KubernetesWorkerPoolsCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_worker_pools_create_scope_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateScopeErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
