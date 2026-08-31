from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateHostnameErrorComponentAttr = Literal["hostname"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateHostnameErrorComponentAttr
] = {
    "hostname",
}


def check_api_v1_secretmanager_managers_archive_create_hostname_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateHostnameErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
