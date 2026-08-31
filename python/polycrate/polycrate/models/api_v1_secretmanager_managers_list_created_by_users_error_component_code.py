from typing import Literal

ApiV1SecretmanagerManagersListCreatedByUsersErrorComponentCode = Literal[
    "invalid_choice", "invalid_list", "invalid_pk_value"
]

API_V1_SECRETMANAGER_MANAGERS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersListCreatedByUsersErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_secretmanager_managers_list_created_by_users_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersListCreatedByUsersErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_LIST_CREATED_BY_USERS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
