from typing import Literal

ApiV1DomainsRegistrarTldPricesListTimeRange = Literal["12h", "1h", "24h", "30d", "6h", "7d", "90d"]

API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_TIME_RANGE_VALUES: set[ApiV1DomainsRegistrarTldPricesListTimeRange] = {
    "12h",
    "1h",
    "24h",
    "30d",
    "6h",
    "7d",
    "90d",
}


def check_api_v1_domains_registrar_tld_prices_list_time_range(
    value: str,
) -> ApiV1DomainsRegistrarTldPricesListTimeRange:
    if value in API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_TIME_RANGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_TIME_RANGE_VALUES!r}"
    )
