from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_worker_pools_update_kind_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateKindErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
