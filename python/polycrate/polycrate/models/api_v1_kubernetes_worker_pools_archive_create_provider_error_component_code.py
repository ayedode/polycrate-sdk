from typing import Literal

ApiV1KubernetesWorkerPoolsArchiveCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsArchiveCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_worker_pools_archive_create_provider_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsArchiveCreateProviderErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
