from typing import Literal

ApiV1PricingProductsCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_PRICING_PRODUCTS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingProductsCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_pricing_products_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1PricingProductsCreateSlaTargetErrorComponentAttr:
    if value in API_V1_PRICING_PRODUCTS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
