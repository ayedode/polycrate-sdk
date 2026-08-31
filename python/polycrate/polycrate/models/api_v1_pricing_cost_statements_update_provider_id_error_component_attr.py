from typing import Literal

ApiV1PricingCostStatementsUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_pricing_cost_statements_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsUpdateProviderIdErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
