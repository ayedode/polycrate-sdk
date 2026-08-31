from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateIsInitializedErrorComponentAttr = Literal["is_initialized"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_IS_INITIALIZED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateIsInitializedErrorComponentAttr
] = {
    "is_initialized",
}


def check_api_v1_secretmanager_managers_archive_create_is_initialized_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateIsInitializedErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_IS_INITIALIZED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_IS_INITIALIZED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
