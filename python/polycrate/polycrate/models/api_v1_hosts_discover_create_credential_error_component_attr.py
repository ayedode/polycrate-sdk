from typing import Literal

ApiV1HostsDiscoverCreateCredentialErrorComponentAttr = Literal["credential"]

API_V1_HOSTS_DISCOVER_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_hosts_discover_create_credential_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateCredentialErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
