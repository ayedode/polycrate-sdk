from typing import Literal

ApiV1ProjectsArchiveCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_PROJECTS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsArchiveCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_projects_archive_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1ProjectsArchiveCreateSloTargetErrorComponentAttr:
    if value in API_V1_PROJECTS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
