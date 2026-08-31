from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OrganizationCachedMetricsEndpoints")


@_attrs_define
class OrganizationCachedMetricsEndpoints:
    """Endpoint rollup; ok = total - down (Spec 630).

    Attributes:
        total (int):
        down (int): Endpoints with state=CRITICAL
        ok (int): Derived as total - down
    """

    total: int
    down: int
    ok: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        down = self.down

        ok = self.ok

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "down": down,
                "ok": ok,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        down = d.pop("down")

        ok = d.pop("ok")

        organization_cached_metrics_endpoints = cls(
            total=total,
            down=down,
            ok=ok,
        )

        organization_cached_metrics_endpoints.additional_properties = d
        return organization_cached_metrics_endpoints

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
