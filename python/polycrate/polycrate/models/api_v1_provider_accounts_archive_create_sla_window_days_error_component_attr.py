from typing import Literal

ApiV1ProviderAccountsArchiveCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsArchiveCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_provider_accounts_archive_create_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsArchiveCreateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
