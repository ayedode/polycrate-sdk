from typing import Literal

ApiV1SecretmanagerManagersUpdateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersUpdateNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_secretmanager_managers_update_name_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateNameErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
