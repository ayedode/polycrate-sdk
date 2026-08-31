from typing import Literal

ApiV1ProjectsPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_PROJECTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_projects_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1ProjectsPartialUpdateKindErrorComponentAttr:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
