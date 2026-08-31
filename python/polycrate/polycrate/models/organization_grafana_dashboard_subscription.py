from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationGrafanaDashboardSubscription")


@_attrs_define
class OrganizationGrafanaDashboardSubscription:
    """Serializer for reading/writing GrafanaDashboard subscriptions of an Organization.

    Create: POST with dashboard (id). revision is optional (null = track latest).
    Update: PATCH enabled / revision only.

        Attributes:
            id (int):
            organization (UUID):
            dashboard (UUID):
            dashboard_display_name (str):
            revision_number (int | None):
            auto_subscribed (bool): Set automatically when the dashboard has is_default=True.
            platform_uid (str): UID of the deployed dashboard in Platform Grafana.
            platform_version (int | None): Grafana version number of the last deployed revision.
            deploy_checksum (str): Checksum of the last successfully deployed revision.
            last_deployed_at (datetime.datetime | None):
            last_deploy_error (str): Last non-fatal deploy error (cleared on success).
            revision (int | None | Unset): Pinned revision, or null to always deploy the latest.
            enabled (bool | Unset): Disabled subscriptions are removed from Platform Grafana on next reconcile.
    """

    id: int
    organization: UUID
    dashboard: UUID
    dashboard_display_name: str
    revision_number: int | None
    auto_subscribed: bool
    platform_uid: str
    platform_version: int | None
    deploy_checksum: str
    last_deployed_at: datetime.datetime | None
    last_deploy_error: str
    revision: int | None | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        organization = str(self.organization)

        dashboard = str(self.dashboard)

        dashboard_display_name = self.dashboard_display_name

        revision_number: int | None
        revision_number = self.revision_number

        auto_subscribed = self.auto_subscribed

        platform_uid = self.platform_uid

        platform_version: int | None
        platform_version = self.platform_version

        deploy_checksum = self.deploy_checksum

        last_deployed_at: None | str
        if isinstance(self.last_deployed_at, datetime.datetime):
            last_deployed_at = self.last_deployed_at.isoformat()
        else:
            last_deployed_at = self.last_deployed_at

        last_deploy_error = self.last_deploy_error

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
                "id": id,
                "organization": organization,
                "dashboard": dashboard,
                "dashboard_display_name": dashboard_display_name,
                "revision_number": revision_number,
                "auto_subscribed": auto_subscribed,
                "platform_uid": platform_uid,
                "platform_version": platform_version,
                "deploy_checksum": deploy_checksum,
                "last_deployed_at": last_deployed_at,
                "last_deploy_error": last_deploy_error,
            }
        )
        if revision is not UNSET:
            field_dict["revision"] = revision
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        organization = UUID(d.pop("organization"))

        dashboard = UUID(d.pop("dashboard"))

        dashboard_display_name = d.pop("dashboard_display_name")

        def _parse_revision_number(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        revision_number = _parse_revision_number(d.pop("revision_number"))

        auto_subscribed = d.pop("auto_subscribed")

        platform_uid = d.pop("platform_uid")

        def _parse_platform_version(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        platform_version = _parse_platform_version(d.pop("platform_version"))

        deploy_checksum = d.pop("deploy_checksum")

        def _parse_last_deployed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_deployed_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_deployed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_deployed_at = _parse_last_deployed_at(d.pop("last_deployed_at"))

        last_deploy_error = d.pop("last_deploy_error")

        def _parse_revision(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        revision = _parse_revision(d.pop("revision", UNSET))

        enabled = d.pop("enabled", UNSET)

        organization_grafana_dashboard_subscription = cls(
            id=id,
            organization=organization,
            dashboard=dashboard,
            dashboard_display_name=dashboard_display_name,
            revision_number=revision_number,
            auto_subscribed=auto_subscribed,
            platform_uid=platform_uid,
            platform_version=platform_version,
            deploy_checksum=deploy_checksum,
            last_deployed_at=last_deployed_at,
            last_deploy_error=last_deploy_error,
            revision=revision,
            enabled=enabled,
        )

        organization_grafana_dashboard_subscription.additional_properties = d
        return organization_grafana_dashboard_subscription

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
