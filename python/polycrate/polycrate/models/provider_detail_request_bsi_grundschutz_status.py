from typing import Literal

ProviderDetailRequestBsiGrundschutzStatus = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_REQUEST_BSI_GRUNDSCHUTZ_STATUS_VALUES: set[ProviderDetailRequestBsiGrundschutzStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_request_bsi_grundschutz_status(value: str) -> ProviderDetailRequestBsiGrundschutzStatus:
    if value in PROVIDER_DETAIL_REQUEST_BSI_GRUNDSCHUTZ_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_BSI_GRUNDSCHUTZ_STATUS_VALUES!r}"
    )
