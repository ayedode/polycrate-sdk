from typing import Literal

ApiV1PricingCostStatementsUpdatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsUpdatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_cost_statements_update_platform_service_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsUpdatePlatformServiceErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
