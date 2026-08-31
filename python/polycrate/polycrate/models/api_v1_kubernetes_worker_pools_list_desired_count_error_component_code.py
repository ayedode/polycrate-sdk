from typing import Literal

ApiV1KubernetesWorkerPoolsListDesiredCountErrorComponentCode = Literal["invalid", "max_value"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_DESIRED_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsListDesiredCountErrorComponentCode
] = {
    "invalid",
    "max_value",
}


def check_api_v1_kubernetes_worker_pools_list_desired_count_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsListDesiredCountErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_DESIRED_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_DESIRED_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
