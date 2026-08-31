from typing import Literal

ApiV1PopsCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_POPS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsCreateDescriptionErrorComponentAttr] = {
    "description",
}


def check_api_v1_pops_create_description_error_component_attr(
    value: str,
) -> ApiV1PopsCreateDescriptionErrorComponentAttr:
    if value in API_V1_POPS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
