from typing import Literal

ApiV1PoliciesDryRunCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_POLICIES_DRY_RUN_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_policies_dry_run_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateProviderIdErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
