from typing import Literal

ApiV1SecretmanagerManagersPartialUpdateAuthMethodsCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_AUTH_METHODS_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersPartialUpdateAuthMethodsCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_secretmanager_managers_partial_update_auth_methods_count_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersPartialUpdateAuthMethodsCountErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_AUTH_METHODS_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_PARTIAL_UPDATE_AUTH_METHODS_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
