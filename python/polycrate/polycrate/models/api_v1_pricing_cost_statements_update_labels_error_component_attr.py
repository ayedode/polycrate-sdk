from typing import Literal

ApiV1PricingCostStatementsUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_pricing_cost_statements_update_labels_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsUpdateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
