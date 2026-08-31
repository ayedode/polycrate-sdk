from typing import Literal

ApiV1SecretmanagerManagersUpdateIsInitializedErrorComponentAttr = Literal["is_initialized"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_IS_INITIALIZED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateIsInitializedErrorComponentAttr
] = {
    "is_initialized",
}


def check_api_v1_secretmanager_managers_update_is_initialized_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateIsInitializedErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_IS_INITIALIZED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_IS_INITIALIZED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
