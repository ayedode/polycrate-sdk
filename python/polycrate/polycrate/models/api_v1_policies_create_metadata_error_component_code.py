from typing import Literal

ApiV1PoliciesCreateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PoliciesCreateMetadataErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_policies_create_metadata_error_component_code(
    value: str,
) -> ApiV1PoliciesCreateMetadataErrorComponentCode:
    if value in API_V1_POLICIES_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
