from typing import Literal

ApiV1HostsReconcileCreateResourceCpuArchitectureErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsReconcileCreateResourceCpuArchitectureErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_hosts_reconcile_create_resource_cpu_architecture_error_component_code(
    value: str,
) -> ApiV1HostsReconcileCreateResourceCpuArchitectureErrorComponentCode:
    if value in API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
