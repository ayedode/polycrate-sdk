from typing import Literal

ApiV1PoliciesCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_POLICIES_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_policies_create_description_error_component_attr(
    value: str,
) -> ApiV1PoliciesCreateDescriptionErrorComponentAttr:
    if value in API_V1_POLICIES_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
