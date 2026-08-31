from typing import Literal

ApiV1PricingCostStatementsGenerateCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_pricing_cost_statements_generate_create_labels_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
