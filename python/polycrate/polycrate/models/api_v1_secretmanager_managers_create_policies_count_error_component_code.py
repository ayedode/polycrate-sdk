from typing import Literal

ApiV1SecretmanagerManagersCreatePoliciesCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_SECRETMANAGER_MANAGERS_CREATE_POLICIES_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersCreatePoliciesCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_secretmanager_managers_create_policies_count_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersCreatePoliciesCountErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_POLICIES_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_POLICIES_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
