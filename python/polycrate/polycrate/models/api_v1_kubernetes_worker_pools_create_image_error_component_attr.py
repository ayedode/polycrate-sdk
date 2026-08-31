from typing import Literal

ApiV1KubernetesWorkerPoolsCreateImageErrorComponentAttr = Literal["image"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_IMAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateImageErrorComponentAttr
] = {
    "image",
}


def check_api_v1_kubernetes_worker_pools_create_image_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateImageErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_IMAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_IMAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
