from typing import Literal

ApiV1RegistryRegistriesListCreatedByUsersErrorComponentCode = Literal[
    "invalid_choice", "invalid_list", "invalid_pk_value"
]

API_V1_REGISTRY_REGISTRIES_LIST_CREATED_BY_USERS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesListCreatedByUsersErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_registry_registries_list_created_by_users_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesListCreatedByUsersErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_LIST_CREATED_BY_USERS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_LIST_CREATED_BY_USERS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
