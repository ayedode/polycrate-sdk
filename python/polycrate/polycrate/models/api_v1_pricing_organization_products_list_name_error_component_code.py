from typing import Literal

ApiV1PricingOrganizationProductsListNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingOrganizationProductsListNameErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_pricing_organization_products_list_name_error_component_code(
    value: str,
) -> ApiV1PricingOrganizationProductsListNameErrorComponentCode:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
