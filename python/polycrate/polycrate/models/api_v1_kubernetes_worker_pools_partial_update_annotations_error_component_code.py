from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_worker_pools_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
