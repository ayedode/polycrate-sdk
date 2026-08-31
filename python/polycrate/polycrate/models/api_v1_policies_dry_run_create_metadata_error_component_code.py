from typing import Literal

ApiV1PoliciesDryRunCreateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_POLICIES_DRY_RUN_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PoliciesDryRunCreateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_policies_dry_run_create_metadata_error_component_code(
    value: str,
) -> ApiV1PoliciesDryRunCreateMetadataErrorComponentCode:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
