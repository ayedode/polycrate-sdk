from typing import Literal

ApiV1PoliciesDryRunCreateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_POLICIES_DRY_RUN_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_policies_dry_run_create_metadata_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateMetadataErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
