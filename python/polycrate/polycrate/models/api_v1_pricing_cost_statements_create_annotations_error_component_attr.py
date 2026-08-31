from typing import Literal

ApiV1PricingCostStatementsCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_COST_STATEMENTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_cost_statements_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
