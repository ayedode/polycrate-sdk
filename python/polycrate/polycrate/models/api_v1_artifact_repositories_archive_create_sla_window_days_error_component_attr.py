from typing import Literal

ApiV1ArtifactRepositoriesArchiveCreateSlaWindowDaysErrorComponentAttr = Literal["sla_window_days"]

API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactRepositoriesArchiveCreateSlaWindowDaysErrorComponentAttr
] = {
    "sla_window_days",
}


def check_api_v1_artifact_repositories_archive_create_sla_window_days_error_component_attr(
    value: str,
) -> ApiV1ArtifactRepositoriesArchiveCreateSlaWindowDaysErrorComponentAttr:
    if value in API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_REPOSITORIES_ARCHIVE_CREATE_SLA_WINDOW_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
