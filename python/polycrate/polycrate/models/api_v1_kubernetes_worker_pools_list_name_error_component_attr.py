from typing import Literal

ApiV1KubernetesWorkerPoolsListNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_WORKER_POOLS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsListNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_worker_pools_list_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsListNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
