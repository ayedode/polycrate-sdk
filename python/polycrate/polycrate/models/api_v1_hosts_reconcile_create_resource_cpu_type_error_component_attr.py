from typing import Literal

ApiV1HostsReconcileCreateResourceCpuTypeErrorComponentAttr = Literal["resource_cpu_type"]

API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_CPU_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateResourceCpuTypeErrorComponentAttr
] = {
    "resource_cpu_type",
}


def check_api_v1_hosts_reconcile_create_resource_cpu_type_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateResourceCpuTypeErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_CPU_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_RESOURCE_CPU_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
