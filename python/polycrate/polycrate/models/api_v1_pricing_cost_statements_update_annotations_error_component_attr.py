from typing import Literal

ApiV1PricingCostStatementsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_cost_statements_update_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
