from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateImageErrorComponentAttr = Literal["image"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_IMAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateImageErrorComponentAttr
] = {
    "image",
}


def check_api_v1_kubernetes_worker_pools_archive_create_image_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateImageErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_IMAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_IMAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
