from typing import Literal

ApiV1PopsListAffectedMaintenancesErrorComponentAttr = Literal["affected_maintenances"]

API_V1_POPS_LIST_AFFECTED_MAINTENANCES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsListAffectedMaintenancesErrorComponentAttr
] = {
    "affected_maintenances",
}


def check_api_v1_pops_list_affected_maintenances_error_component_attr(
    value: str,
) -> ApiV1PopsListAffectedMaintenancesErrorComponentAttr:
    if value in API_V1_POPS_LIST_AFFECTED_MAINTENANCES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_AFFECTED_MAINTENANCES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
