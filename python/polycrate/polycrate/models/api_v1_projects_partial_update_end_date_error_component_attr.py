from typing import Literal

ApiV1ProjectsPartialUpdateEndDateErrorComponentAttr = Literal["end_date"]

API_V1_PROJECTS_PARTIAL_UPDATE_END_DATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsPartialUpdateEndDateErrorComponentAttr
] = {
    "end_date",
}


def check_api_v1_projects_partial_update_end_date_error_component_attr(
    value: str,
) -> ApiV1ProjectsPartialUpdateEndDateErrorComponentAttr:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_END_DATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_END_DATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
