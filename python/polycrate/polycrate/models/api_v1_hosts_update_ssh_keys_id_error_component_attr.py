from typing import Literal

ApiV1HostsUpdateSshKeysIdErrorComponentAttr = Literal["ssh_keys_id"]

API_V1_HOSTS_UPDATE_SSH_KEYS_ID_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsUpdateSshKeysIdErrorComponentAttr] = {
    "ssh_keys_id",
}


def check_api_v1_hosts_update_ssh_keys_id_error_component_attr(
    value: str,
) -> ApiV1HostsUpdateSshKeysIdErrorComponentAttr:
    if value in API_V1_HOSTS_UPDATE_SSH_KEYS_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_SSH_KEYS_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
