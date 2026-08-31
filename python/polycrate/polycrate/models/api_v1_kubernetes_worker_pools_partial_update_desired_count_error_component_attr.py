from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateDesiredCountErrorComponentAttr = Literal["desired_count"]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_DESIRED_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateDesiredCountErrorComponentAttr
] = {
    "desired_count",
}


def check_api_v1_kubernetes_worker_pools_partial_update_desired_count_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateDesiredCountErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_DESIRED_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_DESIRED_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
