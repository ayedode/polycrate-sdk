from typing import Literal

ApiV1HostsReconcileCreateSshKeysIdErrorComponentAttr = Literal["ssh_keys_id"]

API_V1_HOSTS_RECONCILE_CREATE_SSH_KEYS_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsReconcileCreateSshKeysIdErrorComponentAttr
] = {
    "ssh_keys_id",
}


def check_api_v1_hosts_reconcile_create_ssh_keys_id_error_component_attr(
    value: str,
) -> ApiV1HostsReconcileCreateSshKeysIdErrorComponentAttr:
    if value in API_V1_HOSTS_RECONCILE_CREATE_SSH_KEYS_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_SSH_KEYS_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
