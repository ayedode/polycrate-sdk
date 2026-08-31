from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_worker_pools_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
