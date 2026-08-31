from typing import Literal

ApiV1PricingQuotesPartialUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PRICING_QUOTES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesPartialUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_pricing_quotes_partial_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesPartialUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
