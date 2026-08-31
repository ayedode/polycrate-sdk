from typing import Literal

ApiV1OrganizationsPartialUpdateCachedTotalProductCostErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_TOTAL_PRODUCT_COST_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdateCachedTotalProductCostErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_organizations_partial_update_cached_total_product_cost_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdateCachedTotalProductCostErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_TOTAL_PRODUCT_COST_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_TOTAL_PRODUCT_COST_ERROR_COMPONENT_CODE_VALUES!r}"
    )
