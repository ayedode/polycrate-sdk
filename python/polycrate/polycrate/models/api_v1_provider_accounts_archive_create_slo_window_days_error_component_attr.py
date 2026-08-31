from typing import Literal

ApiV1ProviderAccountsArchiveCreateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_api_v1_provider_accounts_archive_create_slo_window_days_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateSloWindowDaysErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
