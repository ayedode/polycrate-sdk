from typing import Literal

ApiV1HostsUpdateCredentialErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_HOSTS_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsUpdateCredentialErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_hosts_update_credential_error_component_code(
    value: str,
) -> ApiV1HostsUpdateCredentialErrorComponentCode:
    if value in API_V1_HOSTS_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
