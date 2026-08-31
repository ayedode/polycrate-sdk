from typing import Literal

ApiV1PricingCostStatementsGenerateCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_pricing_cost_statements_generate_create_display_name_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreateDisplayNameErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
