from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateAuthMethodsCountErrorComponentAttr = Literal["auth_methods_count"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_AUTH_METHODS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateAuthMethodsCountErrorComponentAttr
] = {
    "auth_methods_count",
}


def check_api_v1_secretmanager_managers_archive_create_auth_methods_count_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateAuthMethodsCountErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_AUTH_METHODS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_AUTH_METHODS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
