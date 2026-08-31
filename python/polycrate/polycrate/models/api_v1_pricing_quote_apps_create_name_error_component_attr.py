from typing import Literal

ApiV1PricingQuoteAppsCreateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_QUOTE_APPS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_quote_apps_create_name_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsCreateNameErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
