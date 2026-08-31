from typing import Literal

ApiV1PricingQuotesCreateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_QUOTES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PricingQuotesCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_pricing_quotes_create_name_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesCreateNameErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
