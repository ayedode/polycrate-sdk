from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_worker_pools_update_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
