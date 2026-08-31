from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_kubernetes_worker_pools_archive_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
