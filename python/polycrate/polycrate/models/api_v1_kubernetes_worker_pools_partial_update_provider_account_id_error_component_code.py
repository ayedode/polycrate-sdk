from typing import Literal

ApiV1KubernetesWorkerPoolsPartialUpdateProviderAccountIdErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsPartialUpdateProviderAccountIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_kubernetes_worker_pools_partial_update_provider_account_id_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsPartialUpdateProviderAccountIdErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_PARTIAL_UPDATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
