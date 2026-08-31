from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateArchivedAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_kubernetes_worker_pools_archive_create_archived_at_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateArchivedAtErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
