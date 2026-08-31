from typing import Literal

ApiV1PoliciesDryRunCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_POLICIES_DRY_RUN_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_policies_dry_run_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateTolerationsErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
