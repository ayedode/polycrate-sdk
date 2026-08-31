from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_worker_pools_update_labels_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateLabelsErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
