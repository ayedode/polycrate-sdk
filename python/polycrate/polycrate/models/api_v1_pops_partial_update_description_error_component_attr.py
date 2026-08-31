from typing import Literal

ApiV1PopsPartialUpdateDescriptionErrorComponentAttr = Literal["description"]

API_V1_POPS_PARTIAL_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsPartialUpdateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_pops_partial_update_description_error_component_attr(
    value: str,
) -> ApiV1PopsPartialUpdateDescriptionErrorComponentAttr:
    if value in API_V1_POPS_PARTIAL_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_PARTIAL_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
