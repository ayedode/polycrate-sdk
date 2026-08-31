from typing import Literal

ApiV1ArtifactsUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_ARTIFACTS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_artifacts_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
