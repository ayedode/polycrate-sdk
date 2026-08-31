from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_worker_pools_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
