from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationGrafanaDashboardSubscriptionRequest")


@_attrs_define
class OrganizationGrafanaDashboardSubscriptionRequest:
    """Serializer for reading/writing GrafanaDashboard subscriptions of an Organization.

    Create: POST with dashboard (id). revision is optional (null = track latest).
    Update: PATCH enabled / revision only.

        Attributes:
            organization (UUID):
            dashboard (UUID):
            revision (int | None | Unset): Pinned revision, or null to always deploy the latest.
            enabled (bool | Unset): Disabled subscriptions are removed from Platform Grafana on next reconcile.
    """

    organization: UUID
    dashboard: UUID
    revision: int | None | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization = str(self.organization)

        dashboard = str(self.dashboard)

        revision: int | None | Unset
        if isinstance(self.revision, Unset):
            revision = UNSET
        else:
            revision = self.revision

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization": organization,
                "dashboard": dashboard,
            }
        )
        if revision is not UNSET:
            field_dict["revision"] = revision
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("organization", (None, str(self.organization), "text/plain")))

        files.append(("dashboard", (None, str(self.dashboard), "text/plain")))

        if not isinstance(self.revision, Unset):
            if isinstance(self.revision, int):
                files.append(("revision", (None, str(self.revision).encode(), "text/plain")))
            else:
                files.append(("revision", (None, str(self.revision).encode(), "text/plain")))

        if not isinstance(self.enabled, Unset):
            files.append(("enabled", (None, str(self.enabled).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization = UUID(d.pop("organization"))

        dashboard = UUID(d.pop("dashboard"))

        def _parse_revision(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        revision = _parse_revision(d.pop("revision", UNSET))

        enabled = d.pop("enabled", UNSET)

        organization_grafana_dashboard_subscription_request = cls(
            organization=organization,
            dashboard=dashboard,
            revision=revision,
            enabled=enabled,
        )

        organization_grafana_dashboard_subscription_request.additional_properties = d
        return organization_grafana_dashboard_subscription_request

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
