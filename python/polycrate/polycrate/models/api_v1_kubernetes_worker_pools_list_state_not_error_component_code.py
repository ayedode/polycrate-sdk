from typing import Literal

ApiV1KubernetesWorkerPoolsListStateNotErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsListStateNotErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_worker_pools_list_state_not_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsListStateNotErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_STATE_NOT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
