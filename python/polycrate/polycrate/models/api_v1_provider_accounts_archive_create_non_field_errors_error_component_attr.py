from typing import Literal

ApiV1ProviderAccountsArchiveCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_provider_accounts_archive_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
