from typing import Literal

ApiV1HostsReconcileCreateProviderAccountIdErrorComponentAttr = Literal["provider_account_id"]

API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateProviderAccountIdErrorComponentAttr
] = {
    "provider_account_id",
}


def check_api_v1_hosts_reconcile_create_provider_account_id_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateProviderAccountIdErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_PROVIDER_ACCOUNT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
