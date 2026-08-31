from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_worker_pools_update_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
