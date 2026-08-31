from typing import Literal

ApiV1AlertroutersIngestCreateLabelWorkspaceErrorComponentAttr = Literal["label_workspace"]

API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateLabelWorkspaceErrorComponentAttr
] = {
    "label_workspace",
}


def check_api_v1_alertrouters_ingest_create_label_workspace_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateLabelWorkspaceErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
