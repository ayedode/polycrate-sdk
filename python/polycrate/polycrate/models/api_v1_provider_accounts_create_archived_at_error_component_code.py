from typing import Literal

ApiV1ProviderAccountsCreateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProviderAccountsCreateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_provider_accounts_create_archived_at_error_component_code(
    value: str,
) -> ApiV1ProviderAccountsCreateArchivedAtErrorComponentCode:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
