from typing import Literal

ApiV1KubernetesWorkerPoolsCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_kubernetes_worker_pools_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
