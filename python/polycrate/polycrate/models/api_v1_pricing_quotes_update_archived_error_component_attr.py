from typing import Literal

ApiV1PricingQuotesUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PRICING_QUOTES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_pricing_quotes_update_archived_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesUpdateArchivedErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
