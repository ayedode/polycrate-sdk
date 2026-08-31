from typing import Literal

ApiV1HostsReconcileCreateResourceCpuCoresErrorComponentAttr = Literal["resource_cpu_cores"]

API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateResourceCpuCoresErrorComponentAttr
] = {
    "resource_cpu_cores",
}


def check_api_v1_hosts_reconcile_create_resource_cpu_cores_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateResourceCpuCoresErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_CPU_CORES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
