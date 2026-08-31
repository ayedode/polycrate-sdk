from typing import Literal

ApiV1PricingQuotesArchiveCreateTotalPriceErrorComponentAttr = Literal["total_price"]

API_V1_PRICING_QUOTES_ARCHIVE_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesArchiveCreateTotalPriceErrorComponentAttr
] = {
    "total_price",
}


def check_api_v1_pricing_quotes_archive_create_total_price_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesArchiveCreateTotalPriceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_ARCHIVE_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_ARCHIVE_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
