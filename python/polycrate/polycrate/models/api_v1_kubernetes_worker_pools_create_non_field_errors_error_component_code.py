from typing import Literal

ApiV1KubernetesWorkerPoolsCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_worker_pools_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
