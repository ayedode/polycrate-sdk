from typing import Literal

ApiV1AlertcategoriesCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_ALERTCATEGORIES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_alertcategories_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
