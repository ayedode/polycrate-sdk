from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateImageErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_IMAGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateImageErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_worker_pools_partial_update_image_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateImageErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_IMAGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_IMAGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
