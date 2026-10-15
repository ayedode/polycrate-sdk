from typing import Literal

LbiV2LoadBalancingRequestType = Literal["ConsistentHash", "LeastRequest", "Random", "RoundRobin"]

LBI_V2_LOAD_BALANCING_REQUEST_TYPE_VALUES: set[LbiV2LoadBalancingRequestType] = {
    "ConsistentHash",
    "LeastRequest",
    "Random",
    "RoundRobin",
}


def check_lbi_v2_load_balancing_request_type(value: str) -> LbiV2LoadBalancingRequestType:
    if value in LBI_V2_LOAD_BALANCING_REQUEST_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LBI_V2_LOAD_BALANCING_REQUEST_TYPE_VALUES!r}")
