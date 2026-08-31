from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateSloWindowDaysErrorComponentAttr = Literal["slo_window_days"]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateSloWindowDaysErrorComponentAttr
] = {
    "slo_window_days",
}


def check_api_v1_artifact_repositories_archive_create_slo_window_days_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateSloWindowDaysErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
