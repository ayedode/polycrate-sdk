from typing import Literal

ApiV1HostsReconcileCreateKindErrorComponentAttr = Literal["kind"]

API_V1_HOSTS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsReconcileCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_hosts_reconcile_create_kind_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateKindErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
