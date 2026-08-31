from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_worker_pools_partial_update_provider_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateProviderErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
