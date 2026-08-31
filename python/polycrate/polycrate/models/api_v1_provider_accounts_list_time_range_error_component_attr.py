from typing import Literal

ApiV1ProviderAccountsListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1_PROVIDER_ACCOUNTS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsListTimeRangeErrorComponentAttr
] = {
    "time_range",
}


def check_api_v1_provider_accounts_list_time_range_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsListTimeRangeErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
