from typing import Literal

ApiV1ProviderAccountsUpdateManagedByObjectIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PROVIDER_ACCOUNTS_UPDATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsUpdateManagedByObjectIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_provider_accounts_update_managed_by_object_id_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsUpdateManagedByObjectIdErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
