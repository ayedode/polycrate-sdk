from typing import Literal

ApiV1KubernetesWorkerPoolsListStateErrorComponentAttr = Literal["state"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_kubernetes_worker_pools_list_state_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsListStateErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
