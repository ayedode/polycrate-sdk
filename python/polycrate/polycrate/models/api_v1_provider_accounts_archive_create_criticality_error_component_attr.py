from typing import Literal

ApiV1ProviderAccountsArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_provider_accounts_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
