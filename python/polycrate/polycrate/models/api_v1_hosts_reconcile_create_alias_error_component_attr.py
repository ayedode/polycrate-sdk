from typing import Literal

ApiV1HostsReconcileCreateAliasErrorComponentAttr = Literal["alias"]

API_V1_HOSTS_RECONCILE_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateAliasErrorComponentAttr
] = {
    "alias",
}


def check_api_v1_hosts_reconcile_create_alias_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateAliasErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
