from typing import Literal

ApiV1KubernetesWorkerPoolsCreateSloTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_KUBERNETES_WORKER_POOLS_CREATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesWorkerPoolsCreateSloTargetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_kubernetes_worker_pools_create_slo_target_error_component_code(
    value: str,
) -> ApiV1KubernetesWorkerPoolsCreateSloTargetErrorComponentCode:
    if value in API_V1_KUBERNETES_WORKER_POOLS_CREATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_WORKER_POOLS_CREATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
