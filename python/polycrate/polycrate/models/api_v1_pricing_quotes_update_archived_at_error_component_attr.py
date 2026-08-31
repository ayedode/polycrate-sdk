from typing import Literal

ApiV1PricingQuotesUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PRICING_QUOTES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_pricing_quotes_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
