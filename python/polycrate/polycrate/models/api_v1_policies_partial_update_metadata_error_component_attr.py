from typing import Literal

ApiV1PoliciesPartialUpdateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_POLICIES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesPartialUpdateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_policies_partial_update_metadata_error_component_attr(
    value: str,
) -> ApiV1PoliciesPartialUpdateMetadataErrorComponentAttr:
    if value in API_V1_POLICIES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
