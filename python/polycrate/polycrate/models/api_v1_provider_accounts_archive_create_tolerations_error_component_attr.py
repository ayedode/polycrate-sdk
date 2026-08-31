from typing import Literal

ApiV1ProviderAccountsArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_provider_accounts_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
