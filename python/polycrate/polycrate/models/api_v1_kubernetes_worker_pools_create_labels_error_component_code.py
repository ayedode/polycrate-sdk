from typing import Literal

ApiV1KubernetesWorkerPoolsCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_worker_pools_create_labels_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateLabelsErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
