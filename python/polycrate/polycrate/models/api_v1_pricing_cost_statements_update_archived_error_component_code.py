from typing import Literal

ApiV1PricingCostStatementsUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_cost_statements_update_archived_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsUpdateArchivedErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
