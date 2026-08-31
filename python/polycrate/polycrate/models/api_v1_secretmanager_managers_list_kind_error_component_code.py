from typing import Literal

ApiV1SecretmanagerManagersListKindErrorComponentCode = Literal["invalid_choice", "invalid_list"]

API_V1_SECRETMANAGER_MANAGERS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersListKindErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
}


def check_api_v1_secretmanager_managers_list_kind_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersListKindErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
