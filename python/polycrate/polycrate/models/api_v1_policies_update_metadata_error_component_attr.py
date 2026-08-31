from typing import Literal

ApiV1PoliciesUpdateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_POLICIES_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PoliciesUpdateMetadataErrorComponentAttr] = {
    "metadata",
}


def check_api_v1_policies_update_metadata_error_component_attr(
    value: str,
) -> ApiV1PoliciesUpdateMetadataErrorComponentAttr:
    if value in API_V1_POLICIES_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
