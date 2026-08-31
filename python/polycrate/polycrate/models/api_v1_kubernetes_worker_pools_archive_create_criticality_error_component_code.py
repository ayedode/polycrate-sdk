from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_worker_pools_archive_create_criticality_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateCriticalityErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
