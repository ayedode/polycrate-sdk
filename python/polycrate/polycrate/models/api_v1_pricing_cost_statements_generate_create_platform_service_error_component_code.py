from typing import Literal

ApiV1PricingCostStatementsGenerateCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_cost_statements_generate_create_platform_service_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreatePlatformServiceErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
