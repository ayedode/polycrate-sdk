from typing import Literal

ApiV1ProjectsCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PROJECTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_projects_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1ProjectsCreateTolerationsErrorComponentAttr:
    if value in API_V1_PROJECTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
