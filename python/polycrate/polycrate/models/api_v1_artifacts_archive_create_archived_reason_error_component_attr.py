from typing import Literal

ApiV1ArtifactsArchiveCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_ARTIFACTS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsArchiveCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_artifacts_archive_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1ArtifactsArchiveCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_ARTIFACTS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
