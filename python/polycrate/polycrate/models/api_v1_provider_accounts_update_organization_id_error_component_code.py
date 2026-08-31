from typing import Literal

ApiV1ProviderAccountsUpdateOrganizationIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "required"]

API_V1_PROVIDER_ACCOUNTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsUpdateOrganizationIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "required",
}


def check_api_v1_provider_accounts_update_organization_id_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsUpdateOrganizationIdErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
