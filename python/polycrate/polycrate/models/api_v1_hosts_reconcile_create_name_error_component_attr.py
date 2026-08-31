from typing import Literal

ApiV1HostsReconcileCreateNameErrorComponentAttr = Literal["name"]

API_V1_HOSTS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsReconcileCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_hosts_reconcile_create_name_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateNameErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
