from typing import Literal

ApiV1PricingCostStatementsPartialUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsPartialUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_pricing_cost_statements_partial_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsPartialUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_PARTIAL_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
