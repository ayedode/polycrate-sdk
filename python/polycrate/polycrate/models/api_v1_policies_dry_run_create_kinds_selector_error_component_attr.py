from typing import Literal

ApiV1PoliciesDryRunCreateKindsSelectorErrorComponentAttr = Literal["kinds_selector"]

API_V1_POLICIES_DRY_RUN_CREATE_KINDS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PoliciesDryRunCreateKindsSelectorErrorComponentAttr
] = {
    "kinds_selector",
}


def check_api_v1_policies_dry_run_create_kinds_selector_error_component_attr(
    value: str,
) -> ApiV1PoliciesDryRunCreateKindsSelectorErrorComponentAttr:
    if value in API_V1_POLICIES_DRY_RUN_CREATE_KINDS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POLICIES_DRY_RUN_CREATE_KINDS_SELECTOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
