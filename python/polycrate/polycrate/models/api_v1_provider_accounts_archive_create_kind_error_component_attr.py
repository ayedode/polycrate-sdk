from typing import Literal

ApiV1ProviderAccountsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_provider_accounts_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
