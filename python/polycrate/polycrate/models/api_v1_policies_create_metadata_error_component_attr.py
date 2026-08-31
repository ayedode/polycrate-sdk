from typing import Literal

ApiV1PoliciesCreateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_POLICIES_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PoliciesCreateMetadataErrorComponentAttr] = {
    "metadata",
}


def check_api_v1_policies_create_metadata_error_component_attr(
    value: str,
) -> ApiV1PoliciesCreateMetadataErrorComponentAttr:
    if value in API_V1_POLICIES_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
