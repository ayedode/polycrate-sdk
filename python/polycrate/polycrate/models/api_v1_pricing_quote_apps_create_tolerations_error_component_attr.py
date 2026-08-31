from typing import Literal

ApiV1PricingQuoteAppsCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_QUOTE_APPS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_quote_apps_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsCreateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
