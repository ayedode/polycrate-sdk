from typing import Literal

ApiV1KubernetesWorkerPoolsListKindErrorComponentCode = Literal["invalid_choice", "invalid_list"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsListKindErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
}


def check_api_v1_kubernetes_worker_pools_list_kind_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsListKindErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
