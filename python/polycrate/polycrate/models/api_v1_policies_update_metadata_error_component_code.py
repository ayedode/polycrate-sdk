from typing import Literal

ApiV1PoliciesUpdateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PoliciesUpdateMetadataErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_policies_update_metadata_error_component_code(
    value: str,
) -> ApiV1PoliciesUpdateMetadataErrorComponentCode:
    if value in API_V1_POLICIES_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
