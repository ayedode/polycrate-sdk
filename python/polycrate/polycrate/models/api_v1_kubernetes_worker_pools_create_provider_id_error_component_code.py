from typing import Literal

ApiV1KubernetesWorkerPoolsCreateProviderIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateProviderIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_worker_pools_create_provider_id_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateProviderIdErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_PROVIDER_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
