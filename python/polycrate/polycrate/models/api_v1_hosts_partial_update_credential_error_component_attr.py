from typing import Literal

ApiV1HostsPartialUpdateCredentialErrorComponentAttr = Literal["credential"]

API_V1_HOSTS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_hosts_partial_update_credential_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateCredentialErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
