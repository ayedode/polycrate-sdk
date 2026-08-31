from typing import Literal

ApiV1HostsReconcileCreateCredentialErrorComponentAttr = Literal["credential"]

API_V1_HOSTS_RECONCILE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_hosts_reconcile_create_credential_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateCredentialErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
