from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateDesiredCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_DESIRED_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateDesiredCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_kubernetes_worker_pools_archive_create_desired_count_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateDesiredCountErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_DESIRED_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_DESIRED_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
