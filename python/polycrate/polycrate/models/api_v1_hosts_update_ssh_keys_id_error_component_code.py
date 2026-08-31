from typing import Literal

ApiV1HostsUpdateSshKeysIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_HOSTS_UPDATE_SSH_KEYS_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsUpdateSshKeysIdErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_hosts_update_ssh_keys_id_error_component_code(
    value: str,
) -> ApiV1HostsUpdateSshKeysIdErrorComponentCode:
    if value in API_V1_HOSTS_UPDATE_SSH_KEYS_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_SSH_KEYS_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
