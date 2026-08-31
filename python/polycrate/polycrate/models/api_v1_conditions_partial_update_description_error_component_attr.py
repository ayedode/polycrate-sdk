from typing import Literal

ApiV1ConditionsPartialUpdateDescriptionErrorComponentAttr = Literal["description"]

API_V1_CONDITIONS_PARTIAL_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsPartialUpdateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_conditions_partial_update_description_error_component_attr(
    value: str,
) -> ApiV1ConditionsPartialUpdateDescriptionErrorComponentAttr:
    if value in API_V1_CONDITIONS_PARTIAL_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_PARTIAL_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
