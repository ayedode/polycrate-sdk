from typing import Literal

ApiV1KubernetesWorkerPoolsUpdateProviderReferenceErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_WORKER_POOLS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsUpdateProviderReferenceErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_worker_pools_update_provider_reference_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsUpdateProviderReferenceErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
