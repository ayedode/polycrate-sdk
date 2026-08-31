from typing import Literal

ApiV1PricingOrganizationProductsUpdateObjectIdErrorComponentAttr = Literal["object_id"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsUpdateObjectIdErrorComponentAttr
] = {
    "object_id",
}


def check_api_v1_pricing_organization_products_update_object_id_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsUpdateObjectIdErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_UPDATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
