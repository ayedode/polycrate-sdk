from typing import Literal

ApiV1PricingCostStatementsGenerateCreateReconciliationEnabledErrorComponentAttr = Literal["reconciliation_enabled"]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_pricing_cost_statements_generate_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreateReconciliationEnabledErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
