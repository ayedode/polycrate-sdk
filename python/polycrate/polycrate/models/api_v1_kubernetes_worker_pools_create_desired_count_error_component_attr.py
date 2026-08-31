from typing import Literal

ApiV1KubernetesWorkerPoolsCreateDesiredCountErrorComponentAttr = Literal["desired_count"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_DESIRED_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateDesiredCountErrorComponentAttr
] = {
    "desired_count",
}


def check_api_v1_kubernetes_worker_pools_create_desired_count_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateDesiredCountErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_DESIRED_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_DESIRED_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
