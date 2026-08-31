from typing import Literal

ApiV1AlertcategoriesCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_ALERTCATEGORIES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_alertcategories_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesCreateSlaTargetErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
