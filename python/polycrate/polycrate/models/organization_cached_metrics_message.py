from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.organization_cached_metrics_message_kind_enum import (
    OrganizationCachedMetricsMessageKindEnum,
    check_organization_cached_metrics_message_kind_enum,
)

T = TypeVar("T", bound="OrganizationCachedMetricsMessage")


@_attrs_define
class OrganizationCachedMetricsMessage:
    """Live ops message row for the portal dashboard (Spec 630).

    Attributes:
        kind (OrganizationCachedMetricsMessageKindEnum): * `maintenance` - maintenance
            * `incident` - incident
            * `downtime` - downtime
        id (UUID):
        title (str):
        severity (None | str): Downtime severity when kind=downtime; null for maintenance/incident
        starts_at (datetime.datetime | None):
        ends_at (datetime.datetime | None):
        system_wide (bool): True when organization is null (platform-wide maintenance/incident)
    """

    kind: OrganizationCachedMetricsMessageKindEnum
    id: UUID
    title: str
    severity: None | str
    starts_at: datetime.datetime | None
    ends_at: datetime.datetime | None
    system_wide: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        id = str(self.id)

        title = self.title

        severity: None | str
        severity = self.severity

        starts_at: None | str
        if isinstance(self.starts_at, datetime.datetime):
            starts_at = self.starts_at.isoformat()
        else:
            starts_at = self.starts_at

        ends_at: None | str
        if isinstance(self.ends_at, datetime.datetime):
            ends_at = self.ends_at.isoformat()
        else:
            ends_at = self.ends_at

        system_wide = self.system_wide

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "id": id,
                "title": title,
                "severity": severity,
                "starts_at": starts_at,
                "ends_at": ends_at,
                "system_wide": system_wide,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = check_organization_cached_metrics_message_kind_enum(d.pop("kind"))

        id = UUID(d.pop("id"))

        title = d.pop("title")

        def _parse_severity(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        severity = _parse_severity(d.pop("severity"))

        def _parse_starts_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                starts_at_type_0 = datetime.datetime.fromisoformat(data)

                return starts_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        starts_at = _parse_starts_at(d.pop("starts_at"))

        def _parse_ends_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ends_at_type_0 = datetime.datetime.fromisoformat(data)

                return ends_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        ends_at = _parse_ends_at(d.pop("ends_at"))

        system_wide = d.pop("system_wide")

        organization_cached_metrics_message = cls(
            kind=kind,
            id=id,
            title=title,
            severity=severity,
            starts_at=starts_at,
            ends_at=ends_at,
            system_wide=system_wide,
        )

        organization_cached_metrics_message.additional_properties = d
        return organization_cached_metrics_message

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
