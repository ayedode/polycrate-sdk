from typing import Literal

ApiV1ProvidersListBsiGrundschutzStatus = Literal["no", "planned", "unknown", "yes"]

API_V1_PROVIDERS_LIST_BSI_GRUNDSCHUTZ_STATUS_VALUES: set[ApiV1ProvidersListBsiGrundschutzStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_api_v1_providers_list_bsi_grundschutz_status(value: str) -> ApiV1ProvidersListBsiGrundschutzStatus:
    if value in API_V1_PROVIDERS_LIST_BSI_GRUNDSCHUTZ_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_LIST_BSI_GRUNDSCHUTZ_STATUS_VALUES!r}"
    )
