from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_worker_pools_archive_create_annotations_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateAnnotationsErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
