from typing import Literal

ApiV1PricingQuotesUpdateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_QUOTES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PricingQuotesUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_pricing_quotes_update_name_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesUpdateNameErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
