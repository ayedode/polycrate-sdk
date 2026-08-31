from typing import Literal

ApiV1AlertcategoriesCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_ALERTCATEGORIES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_alertcategories_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesCreateSloTargetErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
