from typing import Literal

ApiV1PricingOrganizationProductsPartialUpdateObjectIdErrorComponentAttr = Literal["object_id"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingOrganizationProductsPartialUpdateObjectIdErrorComponentAttr
] = {
    "object_id",
}


def check_api_v1_pricing_organization_products_partial_update_object_id_error_component_attr(
    value: str,
) -> ApiV1PricingOrganizationProductsPartialUpdateObjectIdErrorComponentAttr:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_PARTIAL_UPDATE_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
