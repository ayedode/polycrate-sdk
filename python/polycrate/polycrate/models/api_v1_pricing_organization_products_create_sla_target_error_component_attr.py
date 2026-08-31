from typing import Literal

ApiV1PricingOrganizationProductsCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_pricing_organization_products_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsCreateSlaTargetErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
