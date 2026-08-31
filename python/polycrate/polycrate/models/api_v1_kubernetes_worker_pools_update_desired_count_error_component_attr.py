from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateDesiredCountErrorComponentAttr = Literal["desired_count"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_DESIRED_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateDesiredCountErrorComponentAttr
] = {
    "desired_count",
}


def check_api_v1_kubernetes_worker_pools_update_desired_count_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateDesiredCountErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_DESIRED_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_DESIRED_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
