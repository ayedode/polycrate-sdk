from typing import Literal

ApiV1KubernetesWorkerPoolsListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_kubernetes_worker_pools_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsListCreatedByComponentErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
