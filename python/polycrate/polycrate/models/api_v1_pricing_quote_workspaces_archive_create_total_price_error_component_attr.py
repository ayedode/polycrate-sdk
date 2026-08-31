from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateTotalPriceErrorComponentAttr = Literal["total_price"]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateTotalPriceErrorComponentAttr
] = {
    "total_price",
}


def check_api_v1_pricing_quote_workspaces_archive_create_total_price_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateTotalPriceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
