from typing import Literal

ApiV1PricingProductsPartialUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsPartialUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_pricing_products_partial_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1PricingProductsPartialUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
