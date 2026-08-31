from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_worker_pools_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
