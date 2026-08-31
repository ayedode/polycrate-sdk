from typing import Literal

ApiV1PoliciesDryRunCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_POLICIES_DRY_RUN_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_policies_dry_run_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
