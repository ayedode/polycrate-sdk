from typing import Literal

ApiV1PopsUpdateDescriptionErrorComponentAttr = Literal["description"]

API_V1_POPS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsUpdateDescriptionErrorComponentAttr] = {
    "description",
}


def check_api_v1_pops_update_description_error_component_attr(
    value: str,
) -> ApiV1PopsUpdateDescriptionErrorComponentAttr:
    if value in API_V1_POPS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
