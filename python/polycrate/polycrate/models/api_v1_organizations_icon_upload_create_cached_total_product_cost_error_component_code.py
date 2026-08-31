from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedTotalProductCostErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_TOTAL_PRODUCT_COST_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedTotalProductCostErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_organizations_icon_upload_create_cached_total_product_cost_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedTotalProductCostErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_TOTAL_PRODUCT_COST_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_TOTAL_PRODUCT_COST_ERROR_COMPONENT_CODE_VALUES!r}"
    )
