from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SloStats")


@_attrs_define
class SloStats:
    """
    Attributes:
        tracked (int): Total monitored objects
        ok (int): Objects meeting SLO (>= 99.5%)
        at_risk (int): Objects at risk (99.0% - 99.5%)
        breached (int): Objects in breach (< 99.0%)
        in_downtime (int): Objects in active downtime
    """

    tracked: int
    ok: int
    at_risk: int
    breached: int
    in_downtime: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracked = self.tracked

        ok = self.ok

        at_risk = self.at_risk

        breached = self.breached

        in_downtime = self.in_downtime

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tracked": tracked,
                "ok": ok,
                "at_risk": at_risk,
                "breached": breached,
                "in_downtime": in_downtime,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tracked = d.pop("tracked")

        ok = d.pop("ok")

        at_risk = d.pop("at_risk")

        breached = d.pop("breached")

        in_downtime = d.pop("in_downtime")

        slo_stats = cls(
            tracked=tracked,
            ok=ok,
            at_risk=at_risk,
            breached=breached,
            in_downtime=in_downtime,
        )

        slo_stats.additional_properties = d
        return slo_stats

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
