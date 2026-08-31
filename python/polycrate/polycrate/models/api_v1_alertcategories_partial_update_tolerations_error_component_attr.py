from typing import Literal

ApiV1AlertcategoriesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_alertcategories_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
