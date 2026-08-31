from typing import Literal

ApiV1PricingQuoteAppsUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PRICING_QUOTE_APPS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_pricing_quote_apps_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
