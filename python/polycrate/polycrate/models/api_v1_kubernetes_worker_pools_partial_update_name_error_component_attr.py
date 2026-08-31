from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_worker_pools_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
