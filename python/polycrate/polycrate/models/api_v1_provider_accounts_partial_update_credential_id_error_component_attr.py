from typing import Literal

ApiV1ProviderAccountsPartialUpdateCredentialIdErrorComponentAttr = Literal["credential_id"]

API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsPartialUpdateCredentialIdErrorComponentAttr
] = {
    "credential_id",
}


def check_api_v1_provider_accounts_partial_update_credential_id_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsPartialUpdateCredentialIdErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_PARTIAL_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
