from typing import Literal

ApiV1PricingRulesCreateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_RULES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PricingRulesCreateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_pricing_rules_create_name_error_component_attr(
    value: str,
) -> ApiV1PricingRulesCreateNameErrorComponentAttr:
    if value in API_V1_PRICING_RULES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_RULES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
