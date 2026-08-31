from typing import Literal

ApiV1PricingQuoteAppsCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PRICING_QUOTE_APPS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_pricing_quote_apps_create_archived_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsCreateArchivedErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
