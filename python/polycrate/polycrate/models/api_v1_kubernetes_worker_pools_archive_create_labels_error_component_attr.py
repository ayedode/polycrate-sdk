from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_kubernetes_worker_pools_archive_create_labels_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateLabelsErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
