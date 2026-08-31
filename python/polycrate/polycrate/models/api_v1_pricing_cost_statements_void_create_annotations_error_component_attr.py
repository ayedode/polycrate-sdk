from typing import Literal

ApiV1PricingCostStatementsVoidCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_cost_statements_void_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
