from typing import Literal

ApiV1HostsArchiveCreateSshKeysIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_HOSTS_ARCHIVE_CREATE_SSH_KEYS_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsArchiveCreateSshKeysIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_hosts_archive_create_ssh_keys_id_error_component_code(
    value: str,
) -> ApiV1HostsArchiveCreateSshKeysIdErrorComponentCode:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_SSH_KEYS_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_SSH_KEYS_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
