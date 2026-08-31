from typing import Literal

ApiV1SecretmanagerManagersPartialUpdateAuthMethodsCountErrorComponentAttr = Literal["auth_methods_count"]

API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_AUTH_METHODS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersPartialUpdateAuthMethodsCountErrorComponentAttr
] = {
    "auth_methods_count",
}


def check_api_v1_secretmanager_managers_partial_update_auth_methods_count_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersPartialUpdateAuthMethodsCountErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_AUTH_METHODS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_AUTH_METHODS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
