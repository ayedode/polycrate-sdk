from typing import Literal

ApiV1HostsDiscoverCreateSshKeysIdErrorComponentAttr = Literal["ssh_keys_id"]

API_V1_HOSTS_DISCOVER_CREATE_SSH_KEYS_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateSshKeysIdErrorComponentAttr
] = {
    "ssh_keys_id",
}


def check_api_v1_hosts_discover_create_ssh_keys_id_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateSshKeysIdErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_SSH_KEYS_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_SSH_KEYS_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
