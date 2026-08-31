from typing import Literal

ApiV1HostsCreateCredentialErrorComponentAttr = Literal["credential"]

API_V1_HOSTS_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsCreateCredentialErrorComponentAttr] = {
    "credential",
}


def check_api_v1_hosts_create_credential_error_component_attr(
    value: str,
) -> ApiV1HostsCreateCredentialErrorComponentAttr:
    if value in API_V1_HOSTS_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
