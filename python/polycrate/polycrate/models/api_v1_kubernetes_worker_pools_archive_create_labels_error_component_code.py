from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_worker_pools_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
