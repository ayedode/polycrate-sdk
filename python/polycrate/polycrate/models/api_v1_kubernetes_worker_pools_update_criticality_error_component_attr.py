from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_worker_pools_update_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
