from typing import Literal

ApiV1HostsReconcileCreateResourceCpuArchitectureErrorComponentAttr = Literal["resource_cpu_architecture"]

API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateResourceCpuArchitectureErrorComponentAttr
] = {
    "resource_cpu_architecture",
}


def check_api_v1_hosts_reconcile_create_resource_cpu_architecture_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateResourceCpuArchitectureErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_CPU_ARCHITECTURE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
