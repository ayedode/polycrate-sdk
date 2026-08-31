from typing import Literal

ApiV1KubernetesWorkerPoolsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_worker_pools_create_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
