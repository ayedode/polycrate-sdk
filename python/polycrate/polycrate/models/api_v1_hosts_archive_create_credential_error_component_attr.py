from typing import Literal

ApiV1HostsArchiveCreateCredentialErrorComponentAttr = Literal["credential"]

API_V1_HOSTS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsArchiveCreateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1_hosts_archive_create_credential_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateCredentialErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
