from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateLocationErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_LOCATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateLocationErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_worker_pools_update_location_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateLocationErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_LOCATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_LOCATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
