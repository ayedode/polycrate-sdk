from typing import Literal

ApiV1OrganizationsIconUploadCreateCachedProductCostUpdatedAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "overflow"
]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_PRODUCT_COST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateCachedProductCostUpdatedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_organizations_icon_upload_create_cached_product_cost_updated_at_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateCachedProductCostUpdatedAtErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_PRODUCT_COST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_CACHED_PRODUCT_COST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
