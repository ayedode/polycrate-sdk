from typing import Literal

ApiV1ProviderAccountsCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_PROVIDER_ACCOUNTS_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_provider_accounts_create_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
