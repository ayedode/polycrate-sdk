from typing import Literal

ApiV1ProviderAccountsArchiveCreateCreatedByUserErrorComponentAttr = Literal["created_by_user"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateCreatedByUserErrorComponentAttr
] = {
    "created_by_user",
}


def check_api_v1_provider_accounts_archive_create_created_by_user_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateCreatedByUserErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
