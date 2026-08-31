from typing import Literal

ApiV1KubernetesWorkerPoolsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_CREATED_BY_COMPONENT_VALUES: set[
    ApiV1KubernetesWorkerPoolsListCreatedByComponent
] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_kubernetes_worker_pools_list_created_by_component(
    value: str,
) -> ApiV1KubernetesWorkerPoolsListCreatedByComponent:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
