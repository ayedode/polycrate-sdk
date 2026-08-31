from typing import Literal

ApiV1PricingQuotesUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_PRICING_QUOTES_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_pricing_quotes_update_display_name_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
