from typing import Literal

ApiV1ProjectsUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PROJECTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_projects_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1ProjectsUpdateTolerationsErrorComponentAttr:
    if value in API_V1_PROJECTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
